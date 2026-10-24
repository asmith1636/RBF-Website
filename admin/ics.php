<?php
// A calendar file for a record's follow-up date: opens in Outlook, Google Calendar or a phone's calendar
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

require_login();
$q = db()->prepare('SELECT * FROM rbf_submissions WHERE id = ? AND follow_up IS NOT NULL');
$q->execute([(int) ($_GET['id'] ?? 0)]);
if (!$s = $q->fetch()) {
    http_response_code(404);
    exit('No follow-up date set.');
}

function ics_text(string $s): string
{
    return str_replace(["\\", "\r\n", "\n", ',', ';'], ["\\\\", '\n', '\n', '\,', '\;'], $s);
}

$who = $s['name'] ?: $s['company'];
$day = str_replace('-', '', $s['follow_up']);
$url = (is_https() ? 'https://' : 'http://') . $_SERVER['HTTP_HOST'] . '/admin/view.php?id=' . $s['id'];
$desc = implode("\n", array_filter([$s['summary'], $s['phone'] ? 'Phone: ' . $s['phone'] : '', $s['email'] ? 'Email: ' . $s['email'] : '', $url]));
$lines = [
    'BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//RBF Construction//Admin//EN', 'BEGIN:VEVENT',
    'UID:rbf-followup-' . $s['id'] . '-' . $day . '@' . $_SERVER['HTTP_HOST'],
    'DTSTAMP:' . gmdate('Ymd\THis\Z'),
    'DTSTART;VALUE=DATE:' . $day, 'DTEND;VALUE=DATE:' . date('Ymd', strtotime($s['follow_up'] . ' +1 day')),
    'SUMMARY:' . ics_text('Follow up: ' . $who . ($s['summary'] ? ' (' . $s['summary'] . ')' : '')),
    'DESCRIPTION:' . ics_text($desc), 'URL:' . $url,
    'BEGIN:VALARM', 'ACTION:DISPLAY', 'DESCRIPTION:' . ics_text('Follow up: ' . $who), 'TRIGGER:PT9H', 'END:VALARM',
    'END:VEVENT', 'END:VCALENDAR',
];
header('Content-Type: text/calendar; charset=utf-8');
header('Content-Disposition: attachment; filename="follow-up-' . $s['id'] . '.ics"');
echo implode("\r\n", $lines) . "\r\n";
