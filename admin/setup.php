<?php
// First visit only: create the first admin account. Needs the setup key from rbf-config.php,
// so nobody else can claim the admin between the deploy and your first login.
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

admin_headers();
if (user_count() > 0) {
    redirect('login.php');
}

$key = (string) (config()['setup_key'] ?? '');
$error = null;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $bucket = 'setup:' . client_key();
    $username = mb_strtolower(post('username'));
    if (too_many($bucket, 5, 900)) {
        $error = 'Too many tries. Wait 15 minutes and try again.';
    } elseif (mb_strlen($key) < 12 || !hash_equals($key, (string) ($_POST['setup_key'] ?? ''))) {
        record_attempt($bucket);
        $error = 'That setup key doesn’t match the one in rbf-config.php.';
    } elseif (!preg_match('/^[a-z0-9._-]{3,40}$/', $username)) {
        $error = 'Usernames are 3–40 letters, numbers, dots, dashes or underscores.';
    } elseif ($problem = password_problem((string) ($_POST['password'] ?? ''), (string) ($_POST['password2'] ?? ''))) {
        $error = $problem;
    } else {
        db()->prepare('INSERT INTO rbf_users (username, password_hash, created_at) VALUES (?, ?, ?)')
            ->execute([$username, password_hash((string) $_POST['password'], PASSWORD_DEFAULT), now()]);
        $q = db()->prepare('SELECT * FROM rbf_users WHERE username = ?');
        $q->execute([$username]);
        log_in($q->fetch());
        flash('Your admin account is ready.');
        redirect('./');
    }
}

top('Set up');
?>
<section class="card narrow">
  <h1>Set up the admin</h1>
  <?php if (mb_strlen($key) < 12): ?>
    <p class="error">Add a <code>setup_key</code> of at least 12 characters to rbf-config.php first.</p>
  <?php else: ?>
    <p>Create the first admin account. You can add more people later under Account.</p>
    <?php if ($error): ?><p class="error"><?= h($error) ?></p><?php endif; ?>
    <form method="post">
      <?= csrf_field() ?>
      <label>Setup key (from rbf-config.php) <input name="setup_key" type="password" required autocomplete="off"></label>
      <label>Username <input name="username" required autocomplete="username" value="<?= h(post('username')) ?>"></label>
      <label>Password (10+ characters) <input name="password" type="password" required minlength="10" autocomplete="new-password"></label>
      <label>Password again <input name="password2" type="password" required minlength="10" autocomplete="new-password"></label>
      <button class="btn">Create account</button>
    </form>
  <?php endif; ?>
</section>
<?php bottom();
