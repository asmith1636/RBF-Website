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
    echo '<p class="empty">That record doesn’t exist (it may have been deleted). <a href="./">Back to the list</a></p>';
    bottom();
    exit;
}
$kind = $s['kind'];
$back = './?kind=' . $kind;

function add_note(int $id, string $author, string $body): void
{
    db()->prepare('INSERT INTO rbf_notes (submission_id, created_at, author, body) VALUES (?, ?, ?, ?)')->execute([$id, now(), $author, $body]);
    db()->prepare('UPDATE rbf_submissions SET updated_at = ? WHERE id = ?')->execute([now(), $id]);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $action = post('action');
    if ($action === 'update') {
        $new = post('status');
        $note = mb_substr(post('note'), 0, 5000);
        if (in_array($new, STATUSES[$kind], true) && $new !== $s['status']) {
            db()->prepare('UPDATE rbf_submissions SET status = ? WHERE id = ?')->execute([$new, $id]);
            add_note($id, $user['username'], "Status changed from {$s['status']} to $new." . ($note !== '' ? "\n\n$note" : ''));
            flash("Marked as $new.");
        } elseif ($note !== '') {
            add_note($id, $user['username'], $note);
            flash('Note added.');
        }
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
$tel = preg_replace('/[^0-9+]/', '', $s['phone']);
$title = $s['name'] ?: $s['company'] ?: 'Submission #' . $id;

top($title, $user, $kind);
?>
<p class="crumb"><a href="<?= h($back) ?>">&larr; <?= h(KINDS[$kind]) ?></a></p>
<div class="head">
  <div>
    <h1><?= h($title) ?></h1>
    <p class="sub"><?= h($s['summary']) ?> &middot; received <?= h(when($s['created_at'])) ?></p>
  </div>
  <span class="status big s-<?= h(strtolower(str_replace(' ', '-', $s['status']))) ?>"><?= h($s['status']) ?></span>
</div>
<p class="actions">
  <?php if ($tel): ?><a class="btn" href="tel:<?= h($tel) ?>">Call <?= h($s['phone']) ?></a><?php endif; ?>
  <?php if ($s['email']): ?><a class="btn ghost" href="mailto:<?= h($s['email']) ?>?subject=<?= rawurlencode('Your request to RBF Construction') ?>">Email <?= h($s['email']) ?></a><?php endif; ?>
</p>

<div class="cols">
  <section class="card">
    <h2>What they sent</h2>
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
  </section>

  <section class="card">
    <h2>Update</h2>
    <form method="post">
      <?= csrf_field() ?><input type="hidden" name="action" value="update">
      <label>Status
        <select name="status">
          <?php foreach (STATUSES[$kind] as $st): ?><option<?= $st === $s['status'] ? ' selected' : '' ?>><?= h($st) ?></option><?php endforeach; ?>
        </select>
      </label>
      <label>Note <textarea name="note" rows="4" placeholder="Called, left voicemail. Site visit Tuesday 10am…"></textarea></label>
      <button class="btn">Save</button>
    </form>

    <h2>History</h2>
    <?php $any = false; foreach ($notes as $n): $any = true; ?>
      <div class="note"><p class="meta"><?= h($n['author']) ?> &middot; <?= h(when($n['created_at'])) ?></p><p><?= nl2br(h($n['body'])) ?></p></div>
    <?php endforeach; if (!$any): ?><p class="muted">No notes yet.</p><?php endif; ?>
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
