<?php
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

require_login();
$kind = array_key_exists($_GET['kind'] ?? '', KINDS) ? $_GET['kind'] : 'quote';
[$where, $args, $order] = filters($kind, $_GET + ['status' => 'all']);  // same filters as the list on screen
$q = db()->prepare("SELECT * FROM rbf_submissions WHERE $where ORDER BY $order");
$q->execute($args);
$rows = $q->fetchAll();
$users = users();

// one column per form field, in the order they first appear
$labels = [];
foreach ($rows as &$r) {
    $r['fields'] = json_decode($r['fields'], true) ?: [];
    foreach (array_keys($r['fields']) as $l) {
        $labels[$l] = true;
    }
}
unset($r);
$labels = array_keys($labels);

$notes = [];
foreach (db()->query('SELECT submission_id, created_at, author, body FROM rbf_notes ORDER BY created_at, id') as $n) {
    $notes[$n['submission_id']][] = date('n/j/Y', strtotime($n['created_at'])) . ' ' . $n['author'] . ': ' . $n['body'];
}

// Spreadsheet apps run cells that start with = + - @ as formulas; prefix those so they stay text
function cell($v): string
{
    $v = (string) $v;
    return preg_match('/^[=+\-@\t\r]/', $v) ? "'" . $v : $v;
}

header('Content-Type: text/csv; charset=utf-8');
header('Content-Disposition: attachment; filename="rbf-' . strtolower(str_replace(' ', '-', KINDS[$kind])) . '-' . date('Y-m-d') . '.csv"');
$out = fopen('php://output', 'w');
fwrite($out, "\xEF\xBB\xBF");  // so Excel reads the file as UTF-8
$extra = $kind === 'quote' ? ['Bid Amount'] : [];
fputcsv($out, array_merge(['ID', 'Received', 'Status', 'Source', 'Assigned To', 'Follow-up'], $extra, $labels, ['Notes']));
foreach ($rows as $r) {
    $line = [$r['id'], date('n/j/Y g:i a', strtotime($r['created_at'])), $r['status'], $r['source'],
             $users[$r['assigned_to']] ?? '', $r['follow_up'] ? date('n/j/Y', strtotime($r['follow_up'])) : ''];
    if ($extra) {
        $line[] = $r['amount'] === null ? '' : (0 + $r['amount']);
    }
    foreach ($labels as $l) {
        $line[] = $r['fields'][$l] ?? '';
    }
    $line[] = implode("\n", $notes[$r['id']] ?? []);
    fputcsv($out, array_map('cell', $line));
}
fclose($out);
