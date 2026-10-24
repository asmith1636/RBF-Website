<?php
// One search box across bid requests, subcontractors and job applications
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

$user = require_login();
$term = trim((string) ($_GET['q'] ?? ''));
$results = [];
if ($term !== '') {
    foreach (array_keys(KINDS) as $k) {
        [$where, $args] = filters($k, ['status' => 'all', 'q' => $term]);
        $q = db()->prepare("SELECT * FROM rbf_submissions WHERE $where ORDER BY created_at DESC LIMIT 50");
        $q->execute($args);
        $results[$k] = $q->fetchAll();
    }
}
$total = array_sum(array_map('count', $results));

top('Search', $user);
?>
<h1>Search</h1>
<form class="search" method="get">
  <input name="q" type="search" placeholder="Name, company, phone or email" value="<?= h($term) ?>" required autofocus>
  <button class="btn">Search all</button>
</form>
<?php if ($term !== '' && !$total): ?><p class="empty">Nothing found for “<?= h($term) ?>”.</p><?php endif; ?>
<?php foreach ($results as $k => $rows): if (!$rows) continue; ?>
  <h2><?= h(KINDS[$k]) ?> <span class="muted">(<?= count($rows) ?>)</span></h2>
  <div class="list">
    <?php foreach ($rows as $r): ?>
      <a class="row simple" href="view.php?id=<?= (int) $r['id'] ?>">
        <span class="who"><strong><?= h($r['name'] ?: $r['company'] ?: '(no name)') ?></strong><?php if ($r['company'] && $r['name']): ?><small><?= h($r['company']) ?></small><?php endif; ?></span>
        <span class="what"><?= h($r['summary']) ?></span>
        <span class="phone"><?= h($r['phone']) ?></span>
        <span class="date"><?= h(date('M j, Y', strtotime($r['created_at']))) ?></span>
        <span class="status <?= status_class($r['status']) ?>"><?= h($r['status']) ?></span>
      </a>
    <?php endforeach; ?>
  </div>
<?php endforeach;
bottom();
