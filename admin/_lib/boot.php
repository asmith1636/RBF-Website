<?php
// Shared code for the RBF admin and the form API. Never served on its own (see .htaccess).
declare(strict_types=1);
defined('RBF') || exit;

date_default_timezone_set('America/Detroit');

const KINDS = ['quote' => 'Bid Requests', 'sub' => 'Subcontractors', 'job' => 'Job Applications'];
const STATUSES = [
    'quote' => ['New', 'Contacted', 'Site Visit', 'Bid Sent', 'Won', 'Lost', 'Not a Fit', 'Spam'],
    'sub'   => ['New', 'Approved', 'On Hold', 'Not a Fit', 'Spam'],
    'job'   => ['New', 'Contacted', 'Interviewed', 'Hired', 'Not a Fit', 'Spam'],
];
const CLOSED = ['Won', 'Lost', 'Not a Fit', 'Hired', 'Spam'];
// The form field shown as each record's one-line summary in the lists, and the one holding the person's name
const SUMMARY_FIELD = ['quote' => 'Project Type', 'sub' => 'Trades / Services', 'job' => 'Position'];
const NAME_FIELD = ['quote' => 'Name', 'sub' => 'Contact Person', 'job' => 'Name'];
const SOURCES = ['Website form', 'Phone call', 'Email', 'Referral', 'Repeat customer', 'Walk-in', 'Job site sign', 'Other'];
const IDLE_LIMIT = 12 * 3600;  // log out after 12 hours without activity

// The same fields and choices as the website forms (build.py), used to add and edit records by hand
const FORM_FIELDS = [
    'quote' => [
        'Name' => ['text'], 'Company' => ['text'], 'Phone' => ['tel'], 'Email' => ['email'],
        'Customer Type' => ['select', ['Homeowner', 'Business owner / developer', 'Franchise operator / brand representative',
                                       'General contractor needing site work', 'Architect / engineer', 'Other']],
        'Project Type' => ['select', ['Custom home / addition', 'Kitchen remodel', 'Bathroom remodel', 'Pole barn / garage',
                                      'Restaurant / drive-thru', 'Retail / commercial building', 'Tenant build-out / office',
                                      'Medical / dental', 'Site development / excavation', 'Underground utilities',
                                      'Parking lot / concrete', 'Demolition', 'Construction management / consulting', 'Other']],
        'Project Location' => ['text'],
        'Timeline' => ['select', ['As soon as possible', '1–3 months', '3–6 months', '6–12 months', '12+ months', 'Just planning']],
        'Drawings' => ['select', ['No drawings yet', 'Concept / sketches', 'Permit-ready drawings', 'Bid set available']],
        'Plans or Photos Link' => ['url'], 'Project Details' => ['textarea'], 'How They Found Us' => ['text'],
    ],
    'sub' => [
        'Company' => ['text'], 'Contact Person' => ['text'], 'Phone' => ['tel'], 'Email' => ['email'],
        'Trades / Services' => ['textarea'], 'Service Area' => ['text'], 'How They Found Us' => ['text'],
    ],
    'job' => [
        'Name' => ['text'], 'Phone' => ['tel'], 'Email' => ['email'],
        'Position' => ['select', ['Laborer', 'Equipment operator', 'Pipe layer', 'Concrete / flatwork', 'CDL driver',
                                  'Foreman / supervisor', 'Project manager / estimator', 'Other']],
        'Experience' => ['textarea'], 'Additional Info' => ['textarea'], 'How They Found Us' => ['text'],
    ],
];

// ---- settings file: lives one folder above the public site, never in the repo
function config(): array
{
    static $c = null;
    if ($c === null) {
        $path = getenv('RBF_CONFIG') ?: dirname(__DIR__, 3) . '/rbf-config.php';
        if (!is_file($path)) {
            http_response_code(503);
            exit('The admin is not set up yet: the settings file rbf-config.php was not found.');
        }
        $c = require $path;
    }
    return $c;
}

function db(): PDO
{
    static $pdo = null;
    if ($pdo === null) {
        $c = config();
        $dsn = 'mysql:host=' . ($c['db_host'] ?? 'localhost') . (isset($c['db_port']) ? ';port=' . $c['db_port'] : '')
             . ';dbname=' . $c['db_name'] . ';charset=utf8mb4';
        $pdo = new PDO($dsn, $c['db_user'], $c['db_pass'], [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]);
        migrate($pdo);
    }
    return $pdo;
}

function migrate(PDO $pdo): void
{
    $v = 0;
    try {
        $v = (int) $pdo->query("SELECT v FROM rbf_settings WHERE k = 'schema'")->fetchColumn();
    } catch (PDOException $e) {
        // first run: no tables yet
    }
    if ($v < 1) {
        migrate_v1($pdo);
    }
    if ($v < 2) {
        // follow-up dates, who's handling it, bid amount, and where the lead came from
        $have = array_column($pdo->query('SHOW COLUMNS FROM rbf_submissions')->fetchAll(), 'Field');
        $add = ['source' => "VARCHAR(40) NOT NULL DEFAULT 'Website form'", 'follow_up' => 'DATE NULL',
                'assigned_to' => 'INT NULL', 'amount' => 'DECIMAL(12,2) NULL'];
        foreach ($add as $col => $def) {
            if (!in_array($col, $have, true)) {
                $pdo->exec("ALTER TABLE rbf_submissions ADD COLUMN $col $def");
            }
        }
        if (!$pdo->query("SHOW INDEX FROM rbf_submissions WHERE Key_name = 'follow'")->fetch()) {
            $pdo->exec('ALTER TABLE rbf_submissions ADD INDEX follow (follow_up)');
        }
        $pdo->exec("UPDATE rbf_settings SET v = '2' WHERE k = 'schema'");
    }
}

function migrate_v1(PDO $pdo): void
{
    $t = 'ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci';
    $pdo->exec("CREATE TABLE IF NOT EXISTS rbf_settings (k VARCHAR(64) PRIMARY KEY, v TEXT NOT NULL) $t");
    $pdo->exec("CREATE TABLE IF NOT EXISTS rbf_users (
        id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(80) NOT NULL UNIQUE, password_hash VARCHAR(255) NOT NULL,
        created_at DATETIME NOT NULL, last_login DATETIME NULL) $t");
    $pdo->exec("CREATE TABLE IF NOT EXISTS rbf_submissions (
        id INT AUTO_INCREMENT PRIMARY KEY, kind VARCHAR(10) NOT NULL, status VARCHAR(30) NOT NULL DEFAULT 'New',
        created_at DATETIME NOT NULL, updated_at DATETIME NOT NULL,
        name VARCHAR(200) NOT NULL DEFAULT '', company VARCHAR(200) NOT NULL DEFAULT '', email VARCHAR(254) NOT NULL DEFAULT '',
        phone VARCHAR(50) NOT NULL DEFAULT '', summary VARCHAR(255) NOT NULL DEFAULT '', fields MEDIUMTEXT NOT NULL,
        INDEX kind_status (kind, status), INDEX created (created_at)) $t");
    $pdo->exec("CREATE TABLE IF NOT EXISTS rbf_notes (
        id INT AUTO_INCREMENT PRIMARY KEY, submission_id INT NOT NULL, created_at DATETIME NOT NULL,
        author VARCHAR(80) NOT NULL, body TEXT NOT NULL, INDEX sub (submission_id),
        FOREIGN KEY (submission_id) REFERENCES rbf_submissions(id) ON DELETE CASCADE) $t");
    $pdo->exec("CREATE TABLE IF NOT EXISTS rbf_attempts (
        id INT AUTO_INCREMENT PRIMARY KEY, bucket VARCHAR(80) NOT NULL, at DATETIME NOT NULL, INDEX bucket_at (bucket, at)) $t");
    $pdo->prepare("INSERT IGNORE INTO rbf_settings (k, v) VALUES ('secret', ?)")->execute([bin2hex(random_bytes(32))]);
    $pdo->exec("INSERT INTO rbf_settings (k, v) VALUES ('schema', '1') ON DUPLICATE KEY UPDATE v = '1'");
}

function now(): string
{
    return date('Y-m-d H:i:s');
}

function secret(): string
{
    static $s = null;
    return $s ??= (string) db()->query("SELECT v FROM rbf_settings WHERE k = 'secret'")->fetchColumn();
}

// ---- rate limits (login, setup, form submissions)
function client_key(): string
{
    // Behind Hostinger's CDN the visitor's address may only be in X-Forwarded-For. This is only used
    // for rate limits, and it's stored as a keyed hash, never as the address itself.
    $fwd = trim(explode(',', $_SERVER['HTTP_X_FORWARDED_FOR'] ?? '')[0]);
    $ip = filter_var($fwd, FILTER_VALIDATE_IP) ? $fwd : ($_SERVER['REMOTE_ADDR'] ?? '');
    return substr(hash_hmac('sha256', $ip, secret()), 0, 32);
}

function too_many(string $bucket, int $max, int $seconds): bool
{
    $db = db();
    $db->prepare('DELETE FROM rbf_attempts WHERE at < ?')->execute([date('Y-m-d H:i:s', time() - 86400)]);
    $q = $db->prepare('SELECT COUNT(*) FROM rbf_attempts WHERE bucket = ? AND at > ?');
    $q->execute([$bucket, date('Y-m-d H:i:s', time() - $seconds)]);
    return (int) $q->fetchColumn() >= $max;
}

function record_attempt(string $bucket): void
{
    db()->prepare('INSERT INTO rbf_attempts (bucket, at) VALUES (?, ?)')->execute([$bucket, now()]);
}

function clear_attempts(string $bucket): void
{
    db()->prepare('DELETE FROM rbf_attempts WHERE bucket = ?')->execute([$bucket]);
}

// ---- admin sessions
function is_https(): bool
{
    return (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || ($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https';
}

function start_session(): void
{
    if (session_status() === PHP_SESSION_ACTIVE) {
        return;
    }
    ini_set('session.use_strict_mode', '1');
    ini_set('session.use_only_cookies', '1');
    session_name('rbf_admin');
    session_set_cookie_params(['lifetime' => 0, 'path' => '/admin', 'secure' => is_https(), 'httponly' => true, 'samesite' => 'Lax']);
    session_start();
}

function admin_headers(): void
{
    header('X-Robots-Tag: noindex, nofollow');
    header('X-Frame-Options: DENY');
    header('X-Content-Type-Options: nosniff');
    header('Referrer-Policy: no-referrer');
    header('Cache-Control: no-store');
    header("Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'none'");
}

function user_count(): int
{
    return (int) db()->query('SELECT COUNT(*) FROM rbf_users')->fetchColumn();
}

function current_user(): ?array
{
    start_session();
    if (empty($_SESSION['uid'])) {
        return null;
    }
    if (time() - ($_SESSION['seen'] ?? 0) > IDLE_LIMIT) {
        end_session();
        return null;
    }
    $q = db()->prepare('SELECT id, username FROM rbf_users WHERE id = ?');
    $q->execute([$_SESSION['uid']]);
    $u = $q->fetch();
    if (!$u) {  // account was removed
        end_session();
        return null;
    }
    $_SESSION['seen'] = time();
    return $u;
}

function require_login(): array
{
    admin_headers();
    $u = current_user();
    if (!$u) {
        redirect(user_count() === 0 ? 'setup.php' : 'login.php');
    }
    return $u;
}

function log_in(array $user): void
{
    start_session();
    session_regenerate_id(true);
    $_SESSION = ['uid' => (int) $user['id'], 'seen' => time(), 'csrf' => bin2hex(random_bytes(32))];
    db()->prepare('UPDATE rbf_users SET last_login = ? WHERE id = ?')->execute([now(), $user['id']]);
}

function end_session(): void
{
    $_SESSION = [];
    if (session_status() === PHP_SESSION_ACTIVE) {
        session_destroy();
    }
    setcookie('rbf_admin', '', ['expires' => time() - 3600, 'path' => '/admin', 'secure' => is_https(), 'httponly' => true, 'samesite' => 'Lax']);
}

// ---- forms
function csrf_token(): string
{
    start_session();
    return $_SESSION['csrf'] ??= bin2hex(random_bytes(32));
}

function csrf_field(): string
{
    return '<input type="hidden" name="csrf" value="' . csrf_token() . '">';
}

function check_csrf(): void
{
    if ($_SERVER['REQUEST_METHOD'] !== 'POST' || !hash_equals(csrf_token(), (string) ($_POST['csrf'] ?? ''))) {
        http_response_code(400);
        exit('This page expired. Go back, reload it and try again.');
    }
}

function flash(?string $msg = null): ?string
{
    start_session();
    if ($msg !== null) {
        $_SESSION['flash'] = $msg;
        return null;
    }
    $m = $_SESSION['flash'] ?? null;
    unset($_SESSION['flash']);
    return $m;
}

function redirect(string $to): never
{
    header('Location: ' . $to, true, 303);
    exit;
}

function h(?string $s): string
{
    return htmlspecialchars((string) $s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function post(string $k): string
{
    return trim((string) ($_POST[$k] ?? ''));
}

function password_problem(string $pw, string $again): ?string
{
    if (mb_strlen($pw) < 10) {
        return 'Use at least 10 characters for the password.';
    }
    if ($pw !== $again) {
        return 'The two passwords don’t match.';
    }
    return null;
}

// ---- page layout
function new_counts(): array
{
    $counts = array_fill_keys(array_keys(KINDS), 0);
    foreach (db()->query("SELECT kind, COUNT(*) n FROM rbf_submissions WHERE status = 'New' GROUP BY kind") as $r) {
        $counts[$r['kind']] = (int) $r['n'];
    }
    return $counts;
}

function top(string $title, ?array $user = null, string $active = ''): void
{
    echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
       . '<meta name="robots" content="noindex, nofollow"><title>' . h($title) . ' | RBF Admin</title>'
       . '<link rel="icon" href="/favicon.ico"><link rel="stylesheet" href="admin.css?v=2"><script src="admin.js?v=2" defer></script></head><body>'
       . '<header class="bar"><a class="brand" href="./">RBF <span>Admin</span></a>';
    if ($user) {
        $counts = new_counts();
        echo '<nav><a href="./"' . ($active === 'home' ? ' class="on"' : '') . '>Dashboard</a>';
        foreach (KINDS as $k => $label) {
            $badge = $counts[$k] ? ' <b class="badge" title="New">' . $counts[$k] . '</b>' : '';
            echo '<a href="list.php?kind=' . $k . '"' . ($active === $k ? ' class="on"' : '') . '>' . h($label) . $badge . '</a>';
        }
        echo '<a href="account.php"' . ($active === 'account' ? ' class="on"' : '') . '>Account</a>'
           . '<form method="post" action="logout.php">' . csrf_field() . '<button class="link">Log out</button></form></nav>';
    }
    echo '</header><main>';
    if ($m = flash()) {
        echo '<p class="flash">' . h($m) . '</p>';
    }
}

function bottom(): void
{
    echo '</main></body></html>';
}

function when(string $dt): string
{
    $t = strtotime($dt);
    return date('M j, Y', $t) . ' at ' . date('g:i a', $t);
}

function day(?string $d): string
{
    return $d ? date('D, M j', strtotime($d)) : '';
}

function money($n): string
{
    return $n === null || $n === '' ? '' : '$' . number_format((float) $n, 0);
}

function status_class(string $s): string
{
    return 's-' . strtolower(str_replace(' ', '-', $s));
}

function valid_date(string $d): ?string
{
    $t = DateTime::createFromFormat('!Y-m-d', $d);
    return $t && $t->format('Y-m-d') === $d ? $d : null;
}

function users(): array
{
    static $u = null;
    return $u ??= array_column(db()->query('SELECT id, username FROM rbf_users ORDER BY username')->fetchAll(), 'username', 'id');
}

function add_note(int $id, string $author, string $body): void
{
    db()->prepare('INSERT INTO rbf_notes (submission_id, created_at, author, body) VALUES (?, ?, ?, ?)')->execute([$id, now(), $author, $body]);
    db()->prepare('UPDATE rbf_submissions SET updated_at = ? WHERE id = ?')->execute([now(), $id]);
}

// Save a record's form fields and the admin-only details. Returns its id.
function save_record(?int $id, string $kind, array $fields, array $meta): int
{
    $fields = array_filter(array_map(fn($v) => trim(mb_substr((string) $v, 0, 5000)), $fields), fn($v) => $v !== '');
    $cols = [
        'name' => mb_substr($fields[NAME_FIELD[$kind]] ?? '', 0, 200),
        'company' => mb_substr($fields['Company'] ?? '', 0, 200),
        'email' => mb_substr($fields['Email'] ?? '', 0, 254),
        'phone' => mb_substr($fields['Phone'] ?? '', 0, 50),
        'summary' => mb_substr(preg_replace('/\s+/', ' ', $fields[SUMMARY_FIELD[$kind]] ?? ''), 0, 120),
        'fields' => json_encode($fields, JSON_UNESCAPED_UNICODE),
        'status' => $meta['status'], 'source' => $meta['source'], 'follow_up' => $meta['follow_up'],
        'assigned_to' => $meta['assigned_to'], 'amount' => $meta['amount'], 'updated_at' => now(),
    ];
    if ($id) {
        $set = implode(', ', array_map(fn($c) => "$c = ?", array_keys($cols)));
        db()->prepare("UPDATE rbf_submissions SET $set WHERE id = ?")->execute([...array_values($cols), $id]);
        return $id;
    }
    $cols += ['kind' => $kind, 'created_at' => $meta['created_at'] ?? now()];
    $marks = implode(', ', array_fill(0, count($cols), '?'));
    db()->prepare('INSERT INTO rbf_submissions (' . implode(', ', array_keys($cols)) . ") VALUES ($marks)")->execute(array_values($cols));
    return (int) db()->lastInsertId();
}

// The list filters, shared by the list page and the CSV download so the download matches what's on screen
function filters(string $kind, array $g): array
{
    $f = [
        'status' => (string) ($g['status'] ?? 'open'), 'q' => trim((string) ($g['q'] ?? '')),
        'from' => valid_date((string) ($g['from'] ?? '')), 'to' => valid_date((string) ($g['to'] ?? '')),
        'type' => (string) ($g['type'] ?? ''), 'source' => (string) ($g['source'] ?? ''),
        'who' => (string) ($g['who'] ?? ''), 'follow' => (string) ($g['follow'] ?? ''), 'sort' => (string) ($g['sort'] ?? 'new'),
    ];
    $where = ['kind = ?'];
    $args = [$kind];
    $open = array_values(array_diff(STATUSES[$kind], CLOSED));
    if ($f['status'] === 'open') {
        $where[] = 'status IN (' . implode(',', array_fill(0, count($open), '?')) . ')';
        array_push($args, ...$open);
    } elseif (in_array($f['status'], STATUSES[$kind], true)) {
        $where[] = 'status = ?';
        $args[] = $f['status'];
    } else {
        $f['status'] = 'all';
    }
    if ($f['q'] !== '') {
        $like = '%' . addcslashes($f['q'], '%_\\') . '%';
        $digits = preg_replace('/\D/', '', $f['q']);
        $where[] = '(name LIKE ? OR company LIKE ? OR email LIKE ? OR phone LIKE ? OR fields LIKE ?'
                 . (strlen($digits) >= 4 ? " OR REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(phone, '-', ''), ' ', ''), '(', ''), ')', ''), '.', '') LIKE ?" : '') . ')';
        array_push($args, $like, $like, $like, $like, $like);
        if (strlen($digits) >= 4) {
            $args[] = "%$digits%";
        }
    }
    if ($f['from']) {
        $where[] = 'created_at >= ?';
        $args[] = $f['from'] . ' 00:00:00';
    }
    if ($f['to']) {
        $where[] = 'created_at <= ?';
        $args[] = $f['to'] . ' 23:59:59';
    }
    $choices = FORM_FIELDS[$kind][SUMMARY_FIELD[$kind]][1] ?? [];
    if ($f['type'] !== '' && in_array($f['type'], $choices, true)) {
        $where[] = 'summary = ?';
        $args[] = $f['type'];
    } else {
        $f['type'] = '';
    }
    if (in_array($f['source'], SOURCES, true)) {
        $where[] = 'source = ?';
        $args[] = $f['source'];
    } else {
        $f['source'] = '';
    }
    if ($f['who'] === 'none') {
        $where[] = 'assigned_to IS NULL';
    } elseif (ctype_digit($f['who'])) {
        $where[] = 'assigned_to = ?';
        $args[] = (int) $f['who'];
    } else {
        $f['who'] = '';
    }
    $today = date('Y-m-d');
    switch ($f['follow']) {
        case 'due':  $where[] = 'follow_up <= ?'; $args[] = $today; break;
        case 'week': $where[] = 'follow_up BETWEEN ? AND ?'; array_push($args, $today, date('Y-m-d', strtotime('+7 days'))); break;
        case 'set':  $where[] = 'follow_up IS NOT NULL'; break;
        case 'none': $where[] = 'follow_up IS NULL'; break;
        default: $f['follow'] = '';
    }
    $orders = ['new' => 'created_at DESC, id DESC', 'old' => 'created_at ASC, id ASC', 'name' => "COALESCE(NULLIF(name, ''), company) ASC",
               'follow' => 'follow_up IS NULL, follow_up ASC', 'amount' => 'amount IS NULL, amount DESC', 'updated' => 'updated_at DESC'];
    if (!isset($orders[$f['sort']])) {
        $f['sort'] = 'new';
    }
    return [implode(' AND ', $where), $args, $orders[$f['sort']], $f];
}

function field_input(string $label, array $def, string $value): string
{
    $name = 'f[' . h($label) . ']';
    $id = 'f-' . strtolower(preg_replace('/[^a-z0-9]+/i', '-', $label));
    $out = '<label for="' . $id . '">' . h($label);
    if ($def[0] === 'textarea') {
        $out .= '<textarea id="' . $id . '" name="' . $name . '" rows="4">' . h($value) . '</textarea>';
    } elseif ($def[0] === 'select') {
        $opts = $def[1];
        if ($value !== '' && !in_array($value, $opts, true)) {
            $opts[] = $value;  // keep an older answer that's no longer a choice
        }
        $out .= '<select id="' . $id . '" name="' . $name . '"><option value="">—</option>';
        foreach ($opts as $o) {
            $out .= '<option' . ($o === $value ? ' selected' : '') . '>' . h($o) . '</option>';
        }
        $out .= '</select>';
    } else {
        $out .= '<input id="' . $id . '" name="' . $name . '" type="' . $def[0] . '" value="' . h($value) . '">';
    }
    return $out . '</label>';
}
