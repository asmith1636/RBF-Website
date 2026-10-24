<?php
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

admin_headers();
if (user_count() === 0) {
    redirect('setup.php');
}
if (current_user()) {
    redirect('./');
}

$error = null;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $username = mb_strtolower(post('username'));
    $ipBucket = 'login-ip:' . client_key();
    $userBucket = 'login-user:' . substr(hash_hmac('sha256', $username, secret()), 0, 32);
    if (too_many($ipBucket, 10, 900) || too_many($userBucket, 5, 900)) {
        $error = 'Too many tries. Wait 15 minutes and try again.';
    } else {
        $q = db()->prepare('SELECT * FROM rbf_users WHERE username = ?');
        $q->execute([$username]);
        $user = $q->fetch();
        // hash something when the user doesn't exist, so both cases take about the same time
        $hash = $user['password_hash'] ?? password_hash(bin2hex(random_bytes(8)), PASSWORD_DEFAULT);
        if (password_verify((string) ($_POST['password'] ?? ''), $hash) && $user) {
            clear_attempts($userBucket);
            if (password_needs_rehash($hash, PASSWORD_DEFAULT)) {
                db()->prepare('UPDATE rbf_users SET password_hash = ? WHERE id = ?')
                    ->execute([password_hash((string) $_POST['password'], PASSWORD_DEFAULT), $user['id']]);
            }
            log_in($user);
            redirect('./');
        }
        record_attempt($ipBucket);
        record_attempt($userBucket);
        $error = 'That username and password don’t match.';
    }
}

top('Log in');
?>
<section class="card narrow">
  <h1>Log in</h1>
  <?php if ($error): ?><p class="error"><?= h($error) ?></p><?php endif; ?>
  <form method="post">
    <?= csrf_field() ?>
    <label>Username <input name="username" autocomplete="username" required autofocus value="<?= h(post('username')) ?>"></label>
    <label>Password <input name="password" type="password" autocomplete="current-password" required></label>
    <button class="btn">Log in</button>
  </form>
</section>
<?php bottom();
