<?php
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

$user = require_login();
$error = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $action = post('action');
    if ($action === 'password') {
        $q = db()->prepare('SELECT password_hash FROM rbf_users WHERE id = ?');
        $q->execute([$user['id']]);
        if (!password_verify((string) ($_POST['current'] ?? ''), (string) $q->fetchColumn())) {
            $error = 'Your current password isn’t right.';
        } elseif ($problem = password_problem((string) ($_POST['password'] ?? ''), (string) ($_POST['password2'] ?? ''))) {
            $error = $problem;
        } else {
            db()->prepare('UPDATE rbf_users SET password_hash = ? WHERE id = ?')
                ->execute([password_hash((string) $_POST['password'], PASSWORD_DEFAULT), $user['id']]);
            flash('Password changed.');
            redirect('account.php');
        }
    } elseif ($action === 'add') {
        $username = mb_strtolower(post('username'));
        $exists = db()->prepare('SELECT COUNT(*) FROM rbf_users WHERE username = ?');
        $exists->execute([$username]);
        if (!preg_match('/^[a-z0-9._-]{3,40}$/', $username)) {
            $error = 'Usernames are 3–40 letters, numbers, dots, dashes or underscores.';
        } elseif ($exists->fetchColumn()) {
            $error = 'That username is taken.';
        } elseif ($problem = password_problem((string) ($_POST['password'] ?? ''), (string) ($_POST['password2'] ?? ''))) {
            $error = $problem;
        } else {
            db()->prepare('INSERT INTO rbf_users (username, password_hash, created_at) VALUES (?, ?, ?)')
                ->execute([$username, password_hash((string) $_POST['password'], PASSWORD_DEFAULT), now()]);
            flash("Added $username. Give them their password in person or by phone, not by email.");
            redirect('account.php');
        }
    } elseif ($action === 'remove') {
        $id = (int) post('id');
        if ($id === (int) $user['id']) {
            $error = 'You can’t remove your own account.';
        } else {
            db()->prepare('DELETE FROM rbf_users WHERE id = ?')->execute([$id]);
            flash('Removed.');
            redirect('account.php');
        }
    }
}

$users = db()->query('SELECT id, username, created_at, last_login FROM rbf_users ORDER BY username')->fetchAll();
top('Account', $user, 'account');
?>
<h1>Account</h1>
<?php if ($error): ?><p class="error"><?= h($error) ?></p><?php endif; ?>
<div class="cols">
  <section class="card">
    <h2>Change your password</h2>
    <p class="muted">Logged in as <strong><?= h($user['username']) ?></strong>.</p>
    <form method="post">
      <?= csrf_field() ?><input type="hidden" name="action" value="password">
      <label>Current password <input name="current" type="password" required autocomplete="current-password"></label>
      <label>New password (10+ characters) <input name="password" type="password" required minlength="10" autocomplete="new-password"></label>
      <label>New password again <input name="password2" type="password" required minlength="10" autocomplete="new-password"></label>
      <button class="btn">Change password</button>
    </form>
  </section>
  <section class="card">
    <h2>People with access</h2>
    <ul class="users">
      <?php foreach ($users as $u): ?>
        <li><span><strong><?= h($u['username']) ?></strong><small>Last login: <?= $u['last_login'] ? h(when($u['last_login'])) : 'never' ?></small></span>
          <?php if ((int) $u['id'] !== (int) $user['id']): ?>
            <form method="post"><?= csrf_field() ?><input type="hidden" name="action" value="remove"><input type="hidden" name="id" value="<?= (int) $u['id'] ?>"><button class="link red">Remove</button></form>
          <?php endif; ?></li>
      <?php endforeach; ?>
    </ul>
    <h2>Add someone</h2>
    <form method="post">
      <?= csrf_field() ?><input type="hidden" name="action" value="add">
      <label>Username <input name="username" required autocomplete="off"></label>
      <label>Password for them (10+ characters) <input name="password" type="password" required minlength="10" autocomplete="new-password"></label>
      <label>Password again <input name="password2" type="password" required minlength="10" autocomplete="new-password"></label>
      <button class="btn">Add</button>
    </form>
  </section>
</div>
<?php bottom();
