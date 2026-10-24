<?php
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

$user = require_login();
$kind = array_key_exists($_GET['kind'] ?? '', KINDS) ? $_GET['kind'] : 'quote';
$statuses = STATUSES[$kind];
$closed = ['Won', 'Lost', 'Not a Fit', 'Hired', 'Spam'];
$open = array_values(array_diff($statuses, $closed));
$status = (string) ($_GET['status'] ?? 'open');
if ($status !== 'open' && $status !== 'all' && !in_array($status, $statuses, true)) {
    $status = 'open';
}
$search = trim((string) ($_GET['q'] ?? ''));
$page = max(1, (int) ($_GET['page'] ?? 1));
$per = 50;

$where = ['kind = ?'];
$args = [$kind];
if ($status === 'open') {
    $where[] = 'status IN (' . implode(',', array_fill(0, count($open), '?')) . ')';
    array_push($args, ...$open);
} elseif ($status !== 'all') {
    $where[] = 'status = ?';
    $args[] = $status;
}
if ($search !== '') {
    $like = '%' . addcslashes($search, '%_\\') . '%';
    $where[] = '(name LIKE ? OR company LIKE ? OR email LIKE ? OR phone LIKE ? OR fields LIKE ?)';
    array_push($args, $like, $like, $like, $like, $like);
}
$sqlWhere = implode(' AND ', $where);
$q = db()->prepare("SELECT COUNT(*) FROM rbf_submissions WHERE $sqlWhere");
$q->execute($args);
$total = (int) $q->fetchColumn();
$q = db()->prepare("SELECT * FROM rbf_submissions WHERE $sqlWhere ORDER BY created_at DESC, id DESC LIMIT $per OFFSET " . (($page - 1) * $per));
$q->execute($args);
$rows = $q->fetchAll();

$counts = ['all' => 0, 'open' => 0];
$c = db()->prepare('SELECT status, COUNT(*) n FROM rbf_submissions WHERE kind = ? GROUP BY status');
$c->execute([$kind]);
foreach ($c as $r) {
    $counts[$r['status']] = (int) $r['n'];
    $counts['all'] += (int) $r['n'];
    if (in_array($r['status'], $open, true)) {
        $counts['open'] += (int) $r['n'];
    }
}

function link_to(array $changes): string
{
    $p = array_merge(['kind' => $_GET['kind'] ?? 'quote', 'status' => $_GET['status'] ?? 'open', 'q' => $_GET['q'] ?? ''], $changes);
    return './?' . http_build_query(array_filter($p, fn($v) => $v !== '' && $v !== null));
}

top(KINDS[$kind], $user, $kind);
?>
<div class="head">
  <h1><?= h(KINDS[$kind]) ?></h1>
  <a class="btn ghost" href="export.php?kind=<?= $kind ?>">Download CSV</a>
</div>
<nav class="tabs">
  <?php foreach (array_merge(['open'], $statuses, ['all']) as $s): ?>
    <a href="<?= h(link_to(['status' => $s, 'page' => null])) ?>"<?= $s === $status ? ' class="on"' : '' ?>><?= h(ucfirst($s)) ?> <span><?= $counts[$s] ?? 0 ?></span></a>
  <?php endforeach; ?>
</nav>
<form class="search" method="get">
  <input type="hidden" name="kind" value="<?= $kind ?>"><input type="hidden" name="status" value="<?= h($status) ?>">
  <input name="q" type="search" placeholder="Search name, company, phone, email or details" value="<?= h($search) ?>">
  <button class="btn">Search</button>
  <?php if ($search !== ''): ?><a href="<?= h(link_to(['q' => null])) ?>">Clear</a><?php endif; ?>
</form>

<?php if (!$rows): ?>
  <p class="empty"><?= $counts['all'] ? 'Nothing matches.' : 'Nothing yet. New submissions from the website show up here.' ?></p>
<?php else: ?>
  <div class="list">
    <?php foreach ($rows as $r): ?>
      <a class="row" href="view.php?id=<?= (int) $r['id'] ?>">
        <span class="who"><strong><?= h($r['name'] ?: $r['company'] ?: '(no name)') ?></strong><?php if ($r['company'] && $r['name']): ?><small><?= h($r['company']) ?></small><?php endif; ?></span>
        <span class="what"><?= h($r['summary']) ?></span>
        <span class="phone"><?= h($r['phone']) ?></span>
        <span class="date"><?= h(date('M j, g:i a', strtotime($r['created_at']))) ?></span>
        <span class="status s-<?= h(strtolower(str_replace(' ', '-', $r['status']))) ?>"><?= h($r['status']) ?></span>
      </a>
    <?php endforeach; ?>
  </div>
  <?php if ($total > $per): ?>
    <p class="pager">
      <?php if ($page > 1): ?><a href="<?= h(link_to(['page' => $page - 1])) ?>">&larr; Newer</a><?php endif; ?>
      <span>Page <?= $page ?> of <?= (int) ceil($total / $per) ?></span>
      <?php if ($page * $per < $total): ?><a href="<?= h(link_to(['page' => $page + 1])) ?>">Older &rarr;</a><?php endif; ?>
    </p>
  <?php endif; ?>
<?php endif;
bottom();
