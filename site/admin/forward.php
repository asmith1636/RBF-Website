<?php
// Email a record to someone: an estimator, a partner, a subcontractor...
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

$user = require_login();
$id = (int) ($_GET['id'] ?? 0);
$q = db()->prepare('SELECT * FROM rbf_submissions WHERE id = ?');
$q->execute([$id]);
if (!$s = $q->fetch()) {
    flash('That record doesn’t exist any more.');
    redirect('./');
}
$who = $s['name'] ?: $s['company'] ?: 'Record #' . $id;
$subject = 'Fwd: ' . ['quote' => 'Bid request', 'sub' => 'Subcontractor', 'job' => 'Job application'][$s['kind']] . ' — ' . $who . ($s['summary'] ? ' (' . $s['summary'] . ')' : '');
$error = null;
$sentTo = [];

// addresses used before, for quick picking
$recent = [];
$r = db()->prepare("SELECT body FROM rbf_notes WHERE body LIKE 'Forwarded to %' ORDER BY id DESC LIMIT 50");
$r->execute();
foreach ($r as $row) {
    if (preg_match('/^Forwarded to (.+?)\.(?:\n|$)/', $row['body'], $m)) {
        foreach (array_map('trim', explode(',', $m[1])) as $e) {
            if (filter_var($e, FILTER_VALIDATE_EMAIL) && count($recent) < 8) {
                $recent[strtolower($e)] = $e;
            }
        }
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $to = array_values(array_unique(array_filter(array_map('trim', preg_split('/[,;\s]+/', post('to'))))));
    $bad = array_filter($to, fn($e) => !filter_var($e, FILTER_VALIDATE_EMAIL));
    $bucket = 'forward:' . $user['id'];
    if (!$to) {
        $error = 'Enter at least one email address.';
    } elseif ($bad) {
        $error = 'These don’t look like email addresses: ' . implode(', ', $bad);
    } elseif (count($to) > 5) {
        $error = 'Forward to 5 people at most at once.';
    } elseif (too_many($bucket, 40, 3600)) {
        $error = 'That’s a lot of forwarding in an hour. Wait a bit and try again.';
    } else {
        $message = trim(mb_substr(post('message'), 0, 3000));
        $link = (is_https() ? 'https://' : 'http://') . $_SERVER['HTTP_HOST'] . '/admin/view.php?id=' . $id;
        $body = ($message !== '' ? $message . "\n\n" : '')
              . "---------- Forwarded by {$user['username']} from the RBF admin ----------\n\n"
              . record_text($s, post('notes') === 'yes')
              . "\n\nOpen in the RBF admin (login required): $link\n";
        $replyTo = post('reply') === 'customer' && filter_var($s['email'], FILTER_VALIDATE_EMAIL) ? $s['email'] : (config()['mail_from'] ?? 'info@rbfconstruction.com');
        record_attempt($bucket);
        if (send_mail($to, $subject, $body, $replyTo)) {
            add_note($id, $user['username'], 'Forwarded to ' . implode(', ', $to) . '.' . ($message !== '' ? "\n\n“" . $message . '”' : ''));
            flash('Sent to ' . implode(', ', $to) . '.');
            redirect('view.php?id=' . $id);
        }
        $error = 'The server couldn’t send the email. Try again, or use “Open in my email app” below.';
    }
}

$plain = record_text($s, true);
$mailto = 'mailto:?subject=' . rawurlencode($subject) . '&body=' . rawurlencode(mb_substr($plain, 0, 1500));
top('Forward ' . $who, $user, $s['kind']);
?>
<p class="crumb"><a href="view.php?id=<?= $id ?>">&larr; Back to <?= h($who) ?></a></p>
<h1>Forward <?= h($who) ?></h1>
<?php if ($error): ?><p class="error"><?= h($error) ?></p><?php endif; ?>
<div class="cols">
  <section class="card">
    <form method="post">
      <?= csrf_field() ?>
      <label>To (separate several with commas)
        <input name="to" type="text" inputmode="email" required autocomplete="email" list="recent-emails" placeholder="estimator@example.com" value="<?= h(post('to')) ?>"></label>
      <?php if ($recent): ?><datalist id="recent-emails"><?php foreach ($recent as $e): ?><option value="<?= h($e) ?>"><?php endforeach; ?></datalist><?php endif; ?>
      <label>Message (optional)
        <textarea name="message" rows="4" placeholder="Can you take a look and price this one by Friday?"><?= h(post('message')) ?></textarea></label>
      <label class="check"><input type="checkbox" name="notes" value="yes"<?= $_SERVER['REQUEST_METHOD'] !== 'POST' || post('notes') === 'yes' ? ' checked' : '' ?>> Include our notes</label>
      <?php if (filter_var($s['email'], FILTER_VALIDATE_EMAIL)): ?>
        <label class="check"><input type="checkbox" name="reply" value="customer"<?= post('reply') === 'customer' ? ' checked' : '' ?>> Replies go straight to <?= h($s['email']) ?> (otherwise to info@)</label>
      <?php endif; ?>
      <p><button class="btn">Send</button></p>
    </form>
    <p class="muted">Sent from info@rbfconstruction.com and logged in this record’s history.
      Or <a href="<?= h($mailto) ?>">open it in my email app</a> instead.</p>
  </section>
  <section class="card">
    <h2>What they’ll get</h2>
    <p class="muted">Subject: <?= h($subject) ?></p>
    <pre class="preview"><?= h($plain) ?></pre>
  </section>
</div>
<?php bottom();
