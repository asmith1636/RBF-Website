<?php
// Saves a website form submission for the admin. The site's script sends a copy here while the
// form itself still goes to FormSubmit for the email, so a lead is kept even if one of them fails.
define('RBF', true);
require __DIR__ . '/../admin/_lib/boot.php';

header('Content-Type: application/json');
header('X-Robots-Tag: noindex');
header('Cache-Control: no-store');

function reply(int $code, array $body): never
{
    http_response_code($code);
    exit(json_encode($body));
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    reply(405, ['ok' => false, 'error' => 'POST only']);
}
// only accept submissions from the site's own pages
$from = $_SERVER['HTTP_ORIGIN'] ?? ($_SERVER['HTTP_REFERER'] ?? '');
if (strcasecmp((string) parse_url($from, PHP_URL_HOST), (string) parse_url('//' . ($_SERVER['HTTP_HOST'] ?? ''), PHP_URL_HOST)) !== 0) {
    reply(403, ['ok' => false, 'error' => 'wrong origin']);
}
$kind = (string) ($_POST['_kind'] ?? '');
if (!array_key_exists($kind, KINDS)) {
    reply(400, ['ok' => false, 'error' => 'unknown form']);
}
if (!empty($_POST['_honey'])) {
    reply(200, ['ok' => true]);  // spam bot filled the hidden field: drop it quietly
}

try {
    $bucket = 'submit:' . client_key();
    if (too_many($bucket, 20, 3600)) {
        reply(429, ['ok' => false, 'error' => 'too many submissions']);
    }
    record_attempt($bucket);

    // PHP turns spaces in field names into underscores; the form's labels never contain underscores
    $fields = [];
    $total = 0;
    foreach ($_POST as $k => $v) {
        if (!is_string($v) || $k === '' || $k[0] === '_' || count($fields) >= 40) {
            continue;
        }
        $label = mb_substr(str_replace('_', ' ', (string) $k), 0, 60);
        $value = trim(mb_substr($v, 0, 5000));
        if ($value === '' || ($total += mb_strlen($value)) > 30000) {
            continue;
        }
        $fields[$label] = $value;
    }
    if (!$fields) {
        reply(400, ['ok' => false, 'error' => 'empty']);
    }

    $name = $fields[$kind === 'sub' ? 'Contact Person' : 'Name'] ?? '';
    $summary = $fields[SUMMARY_FIELD[$kind]] ?? '';
    $now = now();
    db()->prepare('INSERT INTO rbf_submissions (kind, status, created_at, updated_at, name, company, email, phone, summary, fields)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        ->execute([$kind, 'New', $now, $now, mb_substr($name, 0, 200), mb_substr($fields['Company'] ?? '', 0, 200),
                   mb_substr($fields['Email'] ?? '', 0, 254), mb_substr($fields['Phone'] ?? '', 0, 50),
                   mb_substr(preg_replace('/\s+/', ' ', $summary), 0, 120), json_encode($fields, JSON_UNESCAPED_UNICODE)]);
    reply(200, ['ok' => true]);
} catch (Throwable $e) {
    error_log('RBF form save failed: ' . $e->getMessage());
    reply(500, ['ok' => false, 'error' => 'not saved']);
}
