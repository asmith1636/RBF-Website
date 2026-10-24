<?php
// Add a record by hand (a phone call, a referral...) or edit any record
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

$user = require_login();
$id = (int) ($_GET['id'] ?? 0);
$s = null;
if ($id) {
    $q = db()->prepare('SELECT * FROM rbf_submissions WHERE id = ?');
    $q->execute([$id]);
    if (!$s = $q->fetch()) {
        flash('That record doesn’t exist any more.');
        redirect('./');
    }
    $kind = $s['kind'];
} else {
    $kind = array_key_exists($_GET['kind'] ?? '', KINDS) ? $_GET['kind'] : 'quote';
}
$defs = FORM_FIELDS[$kind];
$fields = $s ? (json_decode($s['fields'], true) ?: []) : [];
$meta = $s ? ['status' => $s['status'], 'source' => $s['source'], 'follow_up' => $s['follow_up'], 'assigned_to' => $s['assigned_to'], 'amount' => $s['amount']]
           : ['status' => 'New', 'source' => 'Phone call', 'follow_up' => null, 'assigned_to' => (int) $user['id'], 'amount' => null];
$errors = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $in = (array) ($_POST['f'] ?? []);
    $new = [];
    foreach ($defs as $label => $def) {  // the standard fields, in form order
        $new[$label] = (string) ($in[$label] ?? '');
    }
    foreach ($fields as $label => $v) {   // anything else an older form sent stays as it was
        if (!isset($defs[$label])) {
            $new[$label] = (string) ($in[$label] ?? $v);
        }
    }
    $meta['status'] = in_array(post('status'), STATUSES[$kind], true) ? post('status') : $meta['status'];
    $meta['source'] = in_array(post('source'), SOURCES, true) ? post('source') : 'Other';
    $meta['follow_up'] = post('follow_up') === '' ? null : valid_date(post('follow_up'));
    $who = post('assigned_to');
    $meta['assigned_to'] = $who !== '' && isset(users()[(int) $who]) ? (int) $who : null;
    $amount = str_replace([',', '$', ' '], '', post('amount'));
    $meta['amount'] = $amount === '' ? null : (is_numeric($amount) ? round((float) $amount, 2) : false);
    if (!$s) {
        $received = post('received');
        $meta['created_at'] = $received !== '' && valid_date($received) ? $received . date(' H:i:s') : now();
    }

    if (trim($new[NAME_FIELD[$kind]] ?? '') === '' && trim($new['Company'] ?? '') === '') {
        $errors[] = 'Enter a name or a company.';
    }
    if (trim($new['Email'] ?? '') !== '' && !filter_var(trim($new['Email']), FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'That email address doesn’t look right.';
    }
    if (post('follow_up') !== '' && !$meta['follow_up']) {
        $errors[] = 'The follow-up date isn’t a valid date.';
    }
    if ($meta['amount'] === false) {
        $errors[] = 'Enter the bid amount as a number, like 48500.';
    }

    if (!$errors) {
        if ($s) {
            $changed = [];
            foreach ($new as $label => $v) {
                if (trim($v) !== trim((string) ($fields[$label] ?? ''))) {
                    $changed[] = $label;
                }
            }
            $names = ['status' => 'Status', 'source' => 'Source', 'follow_up' => 'Follow-up date', 'assigned_to' => 'Assigned to', 'amount' => 'Bid amount'];
            foreach ($names as $col => $label) {
                if ((string) $meta[$col] !== (string) $s[$col] && !($col === 'amount' && (float) $meta[$col] === (float) $s[$col] && $s[$col] !== null)) {
                    $changed[] = $label;
                }
            }
            save_record($id, $kind, $new, $meta);
            if ($changed) {
                add_note($id, $user['username'], 'Edited: ' . implode(', ', $changed) . '.'
                    . ($meta['status'] !== $s['status'] ? " Status changed from {$s['status']} to {$meta['status']}." : ''));
            }
            flash($changed ? 'Saved.' : 'No changes.');
        } else {
            $id = save_record(null, $kind, $new, $meta);
            add_note($id, $user['username'], 'Added by hand (' . $meta['source'] . ').');
            if (($note = mb_substr(post('note'), 0, 5000)) !== '') {
                add_note($id, $user['username'], $note);
            }
            flash('Added.');
        }
        redirect('view.php?id=' . $id);
    }
    $fields = $new;
}

$title = $s ? 'Edit ' . ($s['name'] ?: $s['company'] ?: '#' . $id) : 'Add ' . rtrim(['quote' => 'bid request', 'sub' => 'subcontractor', 'job' => 'job applicant'][$kind]);
top($title, $user, $kind);
?>
<p class="crumb"><a href="<?= $s ? 'view.php?id=' . $id : 'list.php?kind=' . $kind ?>">&larr; <?= $s ? 'Back without saving' : h(KINDS[$kind]) ?></a></p>
<h1><?= h($title) ?></h1>
<?php foreach ($errors as $e): ?><p class="error"><?= h($e) ?></p><?php endforeach; ?>
<form method="post" class="cols">
  <?= csrf_field() ?>
  <section class="card">
    <h2>Details</h2>
    <div class="grid2">
      <?php foreach ($defs as $label => $def): ?>
        <div<?= $def[0] === 'textarea' ? ' class="full"' : '' ?>><?= field_input($label, $def, (string) ($fields[$label] ?? '')) ?></div>
      <?php endforeach; ?>
      <?php foreach ($fields as $label => $v): if (isset($defs[$label])) continue; ?>
        <div class="full"><?= field_input((string) $label, ['textarea'], (string) $v) ?></div>
      <?php endforeach; ?>
    </div>
  </section>
  <section class="card">
    <h2>Tracking</h2>
    <label>Status <select name="status"><?php foreach (STATUSES[$kind] as $st): ?><option<?= $st === $meta['status'] ? ' selected' : '' ?>><?= h($st) ?></option><?php endforeach; ?></select></label>
    <label>Source <select name="source"><?php foreach (SOURCES as $src): ?><option<?= $src === $meta['source'] ? ' selected' : '' ?>><?= h($src) ?></option><?php endforeach; ?></select></label>
    <label>Assigned to <select name="assigned_to"><option value="">Nobody</option>
      <?php foreach (users() as $uid => $name): ?><option value="<?= $uid ?>"<?= (int) $meta['assigned_to'] === $uid ? ' selected' : '' ?>><?= h($name) ?></option><?php endforeach; ?></select></label>
    <label>Follow-up date <input name="follow_up" type="date" value="<?= h((string) $meta['follow_up']) ?>"></label>
    <?php if ($kind === 'quote'): ?>
      <label>Bid amount ($) <input name="amount" inputmode="decimal" placeholder="48500" value="<?= h($meta['amount'] === null || $meta['amount'] === false ? post('amount') : (string) (0 + $meta['amount'])) ?>"></label>
    <?php endif; ?>
    <?php if (!$s): ?>
      <label>Date received <input name="received" type="date" value="<?= h(post('received') ?: date('Y-m-d')) ?>"></label>
      <label>First note (optional) <textarea name="note" rows="3" placeholder="Called about a pole barn in Fenton…"><?= h(post('note')) ?></textarea></label>
    <?php endif; ?>
    <button class="btn"><?= $s ? 'Save changes' : 'Add' ?></button>
  </section>
</form>
<?php bottom();
