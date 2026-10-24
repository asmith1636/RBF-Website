<?php
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

$user = require_login();
$id = (int) ($_GET['id'] ?? 0);
$q = db()->prepare('SELECT * FROM rbf_submissions WHERE id = ?');
$q->execute([$id]);
$s = $q->fetch();
if (!$s) {
    http_response_code(404);
    top('Not found', $user);
    echo '<p class="empty">That record doesn’t exist (it may have been deleted). <a href="./">Back to the dashboard</a></p>';
    bottom();
    exit;
}
$kind = $s['kind'];
$back = 'list.php?kind=' . $kind;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $action = post('action');
    if ($action === 'update') {
        $new = post('status');
        $note = mb_substr(post('note'), 0, 5000);
        $follow = post('follow_up') === '' ? null : valid_date(post('follow_up'));
        $parts = [];
        if (in_array($new, STATUSES[$kind], true) && $new !== $s['status']) {
            db()->prepare('UPDATE rbf_submissions SET status = ? WHERE id = ?')->execute([$new, $id]);
            $parts[] = "Status changed from {$s['status']} to $new.";
        }
        if ((post('follow_up') === '' || $follow) && $follow !== $s['follow_up']) {
            db()->prepare('UPDATE rbf_submissions SET follow_up = ? WHERE id = ?')->execute([$follow, $id]);
            $parts[] = $follow ? 'Follow-up set for ' . day($follow) . '.' : 'Follow-up date cleared.';
        }
        if ($note !== '') {
            $parts[] = ($parts ? "\n\n" : '') . $note;
        }
        if ($parts) {
            add_note($id, $user['username'], implode(' ', $parts));
        }
        flash($parts ? 'Saved.' : 'Nothing changed.');
        redirect('view.php?id=' . $id);
    }
    if ($action === 'note') {
        $note = trim(mb_substr(post('note'), 0, 5000));
        if ($note !== '') {
            add_note($id, $user['username'], $note);
        }
        flash($note !== '' ? 'Note added.' : 'Type a note first.');
        redirect('view.php?id=' . $id);
    }
    if ($action === 'snooze') {  // quick follow-up buttons
        $days = (int) post('days');
        if (in_array($days, [1, 3, 7, 14, 30], true)) {
            $follow = date('Y-m-d', strtotime("+$days days"));
            db()->prepare('UPDATE rbf_submissions SET follow_up = ? WHERE id = ?')->execute([$follow, $id]);
            add_note($id, $user['username'], 'Follow-up set for ' . day($follow) . '.');
            flash('Follow-up set for ' . day($follow) . '.');
        }
        redirect('view.php?id=' . $id);
    }
    if ($action === 'delnote') {
        db()->prepare('DELETE FROM rbf_notes WHERE id = ? AND submission_id = ?')->execute([(int) post('note_id'), $id]);
        flash('Note deleted.');
        redirect('view.php?id=' . $id);
    }
    if ($action === 'delete' && post('confirm') === 'yes') {
        db()->prepare('DELETE FROM rbf_submissions WHERE id = ?')->execute([$id]);
        flash('Deleted.');
        redirect($back);
    }
    flash('To delete, tick the box first.');
    redirect('view.php?id=' . $id);
}

$fields = json_decode($s['fields'], true) ?: [];
$notes = db()->prepare('SELECT * FROM rbf_notes WHERE submission_id = ? ORDER BY created_at DESC, id DESC');
$notes->execute([$id]);
$notes = $notes->fetchAll();
$tel = preg_replace('/[^0-9+]/', '', $s['phone']);
$title = $s['name'] ?: $s['company'] ?: 'Record #' . $id;
$today = date('Y-m-d');
$due = $s['follow_up'] && $s['follow_up'] <= $today && !in_array($s['status'], CLOSED, true);

// other records with the same email or phone: repeat customers and duplicates
$digits = substr(preg_replace('/\D/', '', $s['phone']), -10);
$match = [];
$margs = [];
if ($s['email'] !== '') {
    $match[] = 'email = ?';
    $margs[] = $s['email'];
}
if (strlen($digits) >= 7) {
    $match[] = "REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(phone, '-', ''), ' ', ''), '(', ''), ')', ''), '.', '') LIKE ?";
    $margs[] = '%' . $digits;
}
$others = [];
if ($match) {
    $o = db()->prepare('SELECT id, kind, name, company, summary, status, created_at FROM rbf_submissions WHERE id <> ? AND (' . implode(' OR ', $match) . ') ORDER BY created_at DESC LIMIT 10');
    $o->execute([$id, ...$margs]);
    $others = $o->fetchAll();
}

top($title, $user, $kind);
?>
<p class="crumb"><a href="<?= h($back) ?>">&larr; <?= h(KINDS[$kind]) ?></a></p>
<div class="head">
  <div>
    <h1><?= h($title) ?></h1>
    <p class="sub"><?= h(implode(' · ', array_filter([$s['company'] !== $title ? $s['company'] : '', $s['summary'], 'received ' . when($s['created_at']), $s['source'] ?? '']))) ?></p>
  </div>
  <span class="status big <?= status_class($s['status']) ?>"><?= h($s['status']) ?></span>
</div>
<p class="actions">
  <?php if ($tel): ?><a class="btn" href="tel:<?= h($tel) ?>">Call <?= h($s['phone']) ?></a><a class="btn ghost" href="sms:<?= h($tel) ?>">Text</a><?php endif; ?>
  <?php if ($s['email']): ?><a class="btn ghost" href="mailto:<?= h($s['email']) ?>?subject=<?= rawurlencode('Your request to RBF Construction') ?>">Email</a><?php endif; ?>
  <?php if (!empty($fields['Project Location'])): ?><a class="btn ghost" href="https://www.google.com/maps/search/?api=1&amp;query=<?= rawurlencode($fields['Project Location'] . ', MI') ?>" target="_blank" rel="noopener noreferrer">Map</a><?php endif; ?>
  <a class="btn ghost" href="forward.php?id=<?= $id ?>">Forward</a>
  <a class="btn ghost" href="edit.php?id=<?= $id ?>">Edit</a>
</p>

<?php if ($others): ?>
  <div class="notice">
    <strong>Same <?= count($match) > 1 ? 'phone or email' : ($s['email'] !== '' ? 'email' : 'phone') ?> as <?= count($others) ?> other record<?= count($others) > 1 ? 's' : '' ?>:</strong>
    <?php foreach ($others as $o): ?>
      <a href="view.php?id=<?= (int) $o['id'] ?>"><?= h(($o['name'] ?: $o['company']) . ' — ' . ($o['summary'] ?: KINDS[$o['kind']]) . ', ' . date('M j, Y', strtotime($o['created_at'])) . ' (' . $o['status'] . ')') ?></a>
    <?php endforeach; ?>
  </div>
<?php endif; ?>

<div class="cols">
  <section class="card">
    <h2>Details</h2>
    <dl class="fields">
      <?php foreach ($fields as $label => $value): ?>
        <dt><?= h((string) $label) ?></dt>
        <dd><?php
          $v = (string) $value;
          if (preg_match('~^https?://\S+$~i', $v)) {
              echo '<a href="' . h($v) . '" rel="noopener noreferrer nofollow" target="_blank">' . h($v) . '</a>';
          } else {
              echo nl2br(h($v));
          } ?></dd>
      <?php endforeach; ?>
    </dl>
    <h2>Tracking</h2>
    <dl class="fields">
      <dt>Assigned to</dt><dd><?= h(users()[$s['assigned_to']] ?? 'Nobody') ?></dd>
      <dt>Follow-up</dt><dd class="<?= $due ? 'due' : '' ?>"><?= $s['follow_up'] ? h(day($s['follow_up'])) . ($due ? ' — due' : '') . ' &middot; <a href="ics.php?id=' . $id . '">Add to calendar</a>' : 'None' ?></dd>
      <?php if ($kind === 'quote'): ?><dt>Bid amount</dt><dd><?= h(money($s['amount']) ?: '—') ?></dd><?php endif; ?>
      <dt>Source</dt><dd><?= h($s['source'] ?? '') ?></dd>
      <dt>Last updated</dt><dd><?= h(when($s['updated_at'])) ?></dd>
    </dl>
  </section>

  <section class="card">
    <h2>Add a note</h2>
    <form method="post">
      <?= csrf_field() ?><input type="hidden" name="action" value="note">
      <label class="sr" for="note">Note</label>
      <textarea id="note" name="note" rows="4" required placeholder="Called, left voicemail. Site visit Tuesday 10am…"></textarea>
      <p><button class="btn">Add note</button></p>
    </form>

    <h2>Status &amp; follow-up</h2>
    <form method="post">
      <?= csrf_field() ?><input type="hidden" name="action" value="update">
      <label>Status
        <select name="status"><?php foreach (STATUSES[$kind] as $st): ?><option<?= $st === $s['status'] ? ' selected' : '' ?>><?= h($st) ?></option><?php endforeach; ?></select>
      </label>
      <label>Follow-up date <input name="follow_up" type="date" value="<?= h((string) $s['follow_up']) ?>"></label>
      <button class="btn ghost">Save status &amp; follow-up</button>
    </form>
    <form method="post" class="snooze">
      <?= csrf_field() ?><input type="hidden" name="action" value="snooze">
      <span>Follow up in:</span>
      <?php foreach ([1 => 'Tomorrow', 3 => '3 days', 7 => '1 week', 14 => '2 weeks', 30 => '1 month'] as $d => $l): ?>
        <button class="chip" name="days" value="<?= $d ?>"><?= $l ?></button>
      <?php endforeach; ?>
    </form>

    <h2>History</h2>
    <?php foreach ($notes as $n): ?>
      <div class="note"><div class="meta"><?= h($n['author']) ?> &middot; <?= h(when($n['created_at'])) ?>
        <form method="post" class="inline-form"><?= csrf_field() ?><input type="hidden" name="action" value="delnote"><input type="hidden" name="note_id" value="<?= (int) $n['id'] ?>"><button class="link muted" title="Delete this note">delete</button></form></div>
        <p><?= nl2br(h($n['body'])) ?></p></div>
    <?php endforeach; if (!$notes): ?><p class="muted">No notes yet.</p><?php endif; ?>
  </section>
</div>

<details class="danger">
  <summary>Delete this record</summary>
  <form method="post">
    <?= csrf_field() ?><input type="hidden" name="action" value="delete">
    <label class="check"><input type="checkbox" name="confirm" value="yes"> Yes, permanently delete it and its notes</label>
    <button class="btn red">Delete</button>
  </form>
</details>
<?php bottom();
