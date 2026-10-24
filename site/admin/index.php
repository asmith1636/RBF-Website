<?php
// Dashboard: what needs attention today, and how the bids are going
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

$user = require_login();
$db = db();
$today = date('Y-m-d');
$closed = implode(',', array_map(fn($s) => $db->quote($s), CLOSED));

$due = $db->prepare("SELECT * FROM rbf_submissions WHERE follow_up <= ? AND status NOT IN ($closed) ORDER BY follow_up, created_at LIMIT 25");
$due->execute([$today]);
$due = $due->fetchAll();
$fresh = $db->query("SELECT * FROM rbf_submissions WHERE status = 'New' ORDER BY created_at DESC LIMIT 10")->fetchAll();
$mine = $db->prepare("SELECT COUNT(*) FROM rbf_submissions WHERE assigned_to = ? AND status NOT IN ($closed)");
$mine->execute([$user['id']]);
$mine = (int) $mine->fetchColumn();

$year = date('Y') . '-01-01 00:00:00';
function one_row(string $sql, array $a = []): array
{
    $q = db()->prepare($sql);
    $q->execute($a);
    return $q->fetch();
}
$week = one_row("SELECT COUNT(*) n FROM rbf_submissions WHERE kind = 'quote' AND created_at >= ?", [date('Y-m-d 00:00:00', strtotime('-6 days'))]);
$out = one_row("SELECT COUNT(*) n, SUM(amount) total FROM rbf_submissions WHERE kind = 'quote' AND status = 'Bid Sent'");
$won = one_row("SELECT COUNT(*) n, SUM(amount) total FROM rbf_submissions WHERE kind = 'quote' AND status = 'Won' AND created_at >= ?", [$year]);
$lost = one_row("SELECT COUNT(*) n FROM rbf_submissions WHERE kind = 'quote' AND status = 'Lost' AND created_at >= ?", [$year]);
$rate = ($won['n'] + $lost['n']) ? round(100 * $won['n'] / ($won['n'] + $lost['n'])) . '%' : '—';

$pipeline = [];
foreach ($db->query("SELECT status, COUNT(*) n FROM rbf_submissions WHERE kind = 'quote' GROUP BY status") as $r) {
    $pipeline[$r['status']] = (int) $r['n'];
}
$types = $db->prepare("SELECT summary, COUNT(*) n FROM rbf_submissions WHERE kind = 'quote' AND summary <> '' AND created_at >= ? GROUP BY summary ORDER BY n DESC LIMIT 6");
$types->execute([$year]);
$types = $types->fetchAll();
$sources = $db->prepare("SELECT source, COUNT(*) n FROM rbf_submissions WHERE kind = 'quote' AND created_at >= ? GROUP BY source ORDER BY n DESC");
$sources->execute([$year]);
$sources = $sources->fetchAll();
$activity = $db->query('SELECT n.*, s.name, s.company FROM rbf_notes n JOIN rbf_submissions s ON s.id = n.submission_id ORDER BY n.created_at DESC, n.id DESC LIMIT 8')->fetchAll();

function mini_row(array $r, string $extra = ''): string
{
    return '<a class="mini" href="view.php?id=' . (int) $r['id'] . '"><span><strong>' . h($r['name'] ?: $r['company'] ?: '(no name)') . '</strong>'
         . '<small>' . h(KINDS[$r['kind']] . ($r['summary'] ? ' · ' . $r['summary'] : '')) . '</small></span>' . $extra . '</a>';
}

top('Dashboard', $user, 'home');
?>
<div class="head">
  <h1>Hi, <?= h($user['username']) ?></h1>
  <p class="actions">
    <a class="btn" href="edit.php?kind=quote">+ Bid request</a>
    <a class="btn ghost" href="edit.php?kind=sub">+ Subcontractor</a>
    <a class="btn ghost" href="edit.php?kind=job">+ Applicant</a>
  </p>
</div>
<form class="search" method="get" action="search.php">
  <input name="q" type="search" placeholder="Find anyone: name, company, phone or email" required>
  <button class="btn">Search all</button>
</form>

<div class="stats">
  <a class="stat" href="list.php?kind=quote&amp;status=all&amp;from=<?= date('Y-m-d', strtotime('-6 days')) ?>"><b><?= (int) $week['n'] ?></b><span>Bid requests this week</span></a>
  <a class="stat" href="list.php?kind=quote&amp;status=Bid+Sent"><b><?= (int) $out['n'] ?></b><span>Bids out<?= $out['total'] ? ' · ' . h(money($out['total'])) : '' ?></span></a>
  <a class="stat" href="list.php?kind=quote&amp;status=Won&amp;from=<?= date('Y') ?>-01-01"><b><?= (int) $won['n'] ?></b><span>Won in <?= date('Y') ?><?= $won['total'] ? ' · ' . h(money($won['total'])) : '' ?></span></a>
  <div class="stat"><b><?= $rate ?></b><span>Win rate in <?= date('Y') ?> (won vs. lost)</span></div>
</div>

<div class="cols">
  <section class="card">
    <h2>Follow-ups due <?= $due ? '<b class="badge">' . count($due) . '</b>' : '' ?></h2>
    <?php if (!$due): ?><p class="muted">Nothing due today. 🎣</p><?php endif; ?>
    <?php foreach ($due as $r): ?>
      <?= mini_row($r, '<span class="follow due">' . ($r['follow_up'] < $today ? 'Overdue · ' : 'Today · ') . h(day($r['follow_up'])) . '</span>') ?>
    <?php endforeach; ?>
    <h2>New, not yet handled</h2>
    <?php if (!$fresh): ?><p class="muted">You’re all caught up.</p><?php endif; ?>
    <?php foreach ($fresh as $r): ?>
      <?= mini_row($r, '<span class="date">' . h(date('M j', strtotime($r['created_at']))) . '</span>') ?>
    <?php endforeach; ?>
    <?php if ($mine): ?><p><a href="list.php?kind=quote&amp;who=<?= (int) $user['id'] ?>">Your open bid requests (<?= $mine ?>) &rarr;</a></p><?php endif; ?>
  </section>

  <section class="card">
    <h2>Bid request pipeline</h2>
    <?php $max = max([1, ...array_values($pipeline)]); foreach (STATUSES['quote'] as $st): $n = $pipeline[$st] ?? 0; ?>
      <a class="bar-row" href="list.php?kind=quote&amp;status=<?= urlencode($st) ?>"><span><?= h($st) ?></span><i><em class="w<?= (int) round(10 * $n / $max) ?>"></em></i><b><?= $n ?></b></a>
    <?php endforeach; ?>
    <?php if ($types): ?>
      <h2>Top project types in <?= date('Y') ?></h2>
      <?php foreach ($types as $t): ?><a class="bar-row plain" href="list.php?kind=quote&amp;status=all&amp;type=<?= urlencode($t['summary']) ?>"><span><?= h($t['summary']) ?></span><b><?= (int) $t['n'] ?></b></a><?php endforeach; ?>
    <?php endif; ?>
    <?php if ($sources): ?>
      <h2>Where bid requests came from in <?= date('Y') ?></h2>
      <?php foreach ($sources as $t): ?><a class="bar-row plain" href="list.php?kind=quote&amp;status=all&amp;source=<?= urlencode($t['source']) ?>"><span><?= h($t['source']) ?></span><b><?= (int) $t['n'] ?></b></a><?php endforeach; ?>
    <?php endif; ?>
    <h2>Recent activity</h2>
    <?php if (!$activity): ?><p class="muted">No activity yet.</p><?php endif; ?>
    <?php foreach ($activity as $n): ?>
      <a class="mini" href="view.php?id=<?= (int) $n['submission_id'] ?>"><span><strong><?= h($n['name'] ?: $n['company']) ?></strong><small><?= h($n['author'] . ': ' . mb_strimwidth(str_replace("\n", ' ', $n['body']), 0, 90, '…')) ?></small></span><span class="date"><?= h(date('M j', strtotime($n['created_at']))) ?></span></a>
    <?php endforeach; ?>
  </section>
</div>
<?php bottom();
