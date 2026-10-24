<?php
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

$user = require_login();
$kind = array_key_exists($_GET['kind'] ?? '', KINDS) ? $_GET['kind'] : 'quote';
$statuses = STATUSES[$kind];
$open = array_values(array_diff($statuses, CLOSED));
[$where, $args, $order, $f] = filters($kind, $_GET);
$page = max(1, (int) ($_GET['page'] ?? 1));
$per = 50;

// bulk actions on the ticked rows
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $ids = array_values(array_filter(array_map('intval', (array) ($_POST['ids'] ?? []))));
    $back = 'list.php?' . (string) ($_POST['back'] ?? '');
    if (!$ids) {
        flash('Tick at least one row first.');
        redirect($back);
    }
    $in = implode(',', array_fill(0, count($ids), '?'));
    $rows = db()->prepare("SELECT id, status, assigned_to FROM rbf_submissions WHERE kind = ? AND id IN ($in)");
    $rows->execute([$kind, ...$ids]);
    $rows = $rows->fetchAll();
    $action = post('bulk');
    $n = count($rows);
    if (str_starts_with($action, 'status:') && in_array($new = substr($action, 7), $statuses, true)) {
        foreach ($rows as $r) {
            if ($r['status'] !== $new) {
                db()->prepare('UPDATE rbf_submissions SET status = ? WHERE id = ?')->execute([$new, $r['id']]);
                add_note((int) $r['id'], $user['username'], "Status changed from {$r['status']} to $new.");
            }
        }
        flash("Marked $n as $new.");
    } elseif (str_starts_with($action, 'assign:')) {
        $to = substr($action, 7);
        $uid = $to === 'none' ? null : (int) $to;
        if ($uid === null || isset(users()[$uid])) {
            foreach ($rows as $r) {
                db()->prepare('UPDATE rbf_submissions SET assigned_to = ? WHERE id = ?')->execute([$uid, $r['id']]);
                add_note((int) $r['id'], $user['username'], $uid ? 'Assigned to ' . users()[$uid] . '.' : 'Unassigned.');
            }
            flash($uid ? "Assigned $n to " . users()[$uid] . '.' : "Unassigned $n.");
        }
    } elseif ($action === 'delete') {
        if (post('confirm') !== 'yes') {
            flash('To delete, also tick “Yes, delete”.');
        } else {
            db()->prepare("DELETE FROM rbf_submissions WHERE kind = ? AND id IN ($in)")->execute([$kind, ...$ids]);
            flash("Deleted $n.");
        }
    } else {
        flash('Choose an action first.');
    }
    redirect($back);
}

$q = db()->prepare("SELECT COUNT(*) FROM rbf_submissions WHERE $where");
$q->execute($args);
$total = (int) $q->fetchColumn();
$q = db()->prepare("SELECT * FROM rbf_submissions WHERE $where ORDER BY $order LIMIT $per OFFSET " . (($page - 1) * $per));
$q->execute($args);
$rows = $q->fetchAll();

// counts per status tab, with the other filters applied
$tabs = ['open' => 0, 'all' => 0];
[$w2, $a2] = filters($kind, array_merge($_GET, ['status' => 'all']));
$c = db()->prepare("SELECT status, COUNT(*) n FROM rbf_submissions WHERE $w2 GROUP BY status");
$c->execute($a2);
foreach ($c as $r) {
    $tabs[$r['status']] = (int) $r['n'];
    $tabs['all'] += (int) $r['n'];
    if (in_array($r['status'], $open, true)) {
        $tabs['open'] += (int) $r['n'];
    }
}

$params = array_filter(['kind' => $kind] + $f, fn($v) => $v !== '' && $v !== null);
unset($params['sort']);
if ($f['sort'] !== 'new') {
    $params['sort'] = $f['sort'];
}
function link_with(array $params, array $changes): string
{
    return 'list.php?' . http_build_query(array_filter(array_merge($params, $changes), fn($v) => $v !== '' && $v !== null));
}
$filtered = $f['q'] !== '' || $f['from'] || $f['to'] || $f['type'] !== '' || $f['source'] !== '' || $f['who'] !== '' || $f['follow'] !== '';
$typeLabel = SUMMARY_FIELD[$kind];
$typeChoices = FORM_FIELDS[$kind][$typeLabel][1] ?? [];
$today = date('Y-m-d');

top(KINDS[$kind], $user, $kind);
?>
<div class="head">
  <h1><?= h(KINDS[$kind]) ?></h1>
  <p class="actions">
    <a class="btn" href="edit.php?kind=<?= $kind ?>">+ Add new</a>
    <a class="btn ghost" href="<?= h('export.php?' . http_build_query($params + ['status' => $f['status']])) ?>">Download CSV<?= $filtered ? ' (filtered)' : '' ?></a>
  </p>
</div>
<nav class="tabs">
  <?php foreach (array_merge(['open'], $statuses, ['all']) as $s): ?>
    <a href="<?= h(link_with($params, ['status' => $s, 'page' => null])) ?>"<?= $s === $f['status'] ? ' class="on"' : '' ?>><?= h(ucfirst($s)) ?> <span><?= $tabs[$s] ?? 0 ?></span></a>
  <?php endforeach; ?>
</nav>

<form class="filters" method="get">
  <input type="hidden" name="kind" value="<?= $kind ?>"><input type="hidden" name="status" value="<?= h($f['status']) ?>">
  <input class="grow" name="q" type="search" placeholder="Search name, company, phone, email or details" value="<?= h($f['q']) ?>">
  <?php if ($typeChoices): ?>
    <select name="type" title="<?= h($typeLabel) ?>"><option value=""><?= h($typeLabel) ?>: all</option>
      <?php foreach ($typeChoices as $t): ?><option<?= $t === $f['type'] ? ' selected' : '' ?>><?= h($t) ?></option><?php endforeach; ?></select>
  <?php endif; ?>
  <select name="source" title="Source"><option value="">Source: all</option>
    <?php foreach (SOURCES as $s): ?><option<?= $s === $f['source'] ? ' selected' : '' ?>><?= h($s) ?></option><?php endforeach; ?></select>
  <select name="who" title="Assigned to"><option value="">Assigned: anyone</option><option value="none"<?= $f['who'] === 'none' ? ' selected' : '' ?>>Not assigned</option>
    <?php foreach (users() as $id => $name): ?><option value="<?= $id ?>"<?= (string) $id === $f['who'] ? ' selected' : '' ?>><?= h($name) ?></option><?php endforeach; ?></select>
  <select name="follow" title="Follow-up">
    <?php foreach (['' => 'Follow-up: any', 'due' => 'Follow-up due or overdue', 'week' => 'Follow-up in the next 7 days', 'set' => 'Has a follow-up date', 'none' => 'No follow-up date'] as $k => $l): ?>
      <option value="<?= $k ?>"<?= $k === $f['follow'] ? ' selected' : '' ?>><?= h($l) ?></option><?php endforeach; ?></select>
  <label class="inline">From <input name="from" type="date" value="<?= h($f['from']) ?>"></label>
  <label class="inline">To <input name="to" type="date" value="<?= h($f['to']) ?>"></label>
  <select name="sort" title="Sort">
    <?php foreach (['new' => 'Newest first', 'old' => 'Oldest first', 'updated' => 'Recently updated', 'follow' => 'Follow-up date', 'name' => 'Name A–Z'] + ($kind === 'quote' ? ['amount' => 'Bid amount'] : []) as $k => $l): ?>
      <option value="<?= $k ?>"<?= $k === $f['sort'] ? ' selected' : '' ?>><?= h($l) ?></option><?php endforeach; ?></select>
  <button class="btn">Apply</button>
  <?php if ($filtered || $f['sort'] !== 'new'): ?><a href="list.php?kind=<?= $kind ?>&amp;status=<?= h($f['status']) ?>">Clear filters</a><?php endif; ?>
</form>

<?php if (!$rows): ?>
  <p class="empty"><?= $tabs['all'] || $filtered ? 'Nothing matches these filters.' : 'Nothing yet. New submissions from the website show up here, or use “Add new”.' ?></p>
<?php else: ?>
  <form method="post" class="bulk">
    <?= csrf_field() ?><input type="hidden" name="back" value="<?= h(http_build_query(array_merge($params, ['status' => $f['status'], 'page' => $page > 1 ? $page : null]))) ?>">
    <div class="list">
      <div class="row headrow">
        <label class="tick" title="Select all"><input type="checkbox" data-all></label>
        <span>Name</span><span><?= h($typeLabel) ?></span><span><?= $kind === 'quote' ? 'Bid / Phone' : 'Phone' ?></span><span>Follow-up</span><span>Received</span><span>Status</span>
      </div>
      <?php foreach ($rows as $r): $due = $r['follow_up'] && $r['follow_up'] <= $today && !in_array($r['status'], CLOSED, true); ?>
        <div class="row">
          <label class="tick"><input type="checkbox" name="ids[]" value="<?= (int) $r['id'] ?>"></label>
          <a class="who" href="view.php?id=<?= (int) $r['id'] ?>"><strong><?= h($r['name'] ?: $r['company'] ?: '(no name)') ?></strong><?php if ($r['company'] && $r['name']): ?><small><?= h($r['company']) ?></small><?php endif; ?></a>
          <span class="what"><?= h($r['summary']) ?><?php if ($r['assigned_to'] && isset(users()[$r['assigned_to']])): ?><small>&rarr; <?= h(users()[$r['assigned_to']]) ?></small><?php endif; ?></span>
          <span class="phone"><?= h($kind === 'quote' ? (money($r['amount']) ?: $r['phone']) : $r['phone']) ?></span>
          <span class="follow<?= $due ? ' due' : '' ?>"><?= h(day($r['follow_up'])) ?></span>
          <span class="date"><?= h(date('M j, Y', strtotime($r['created_at']))) ?></span>
          <span class="status <?= status_class($r['status']) ?>"><?= h($r['status']) ?></span>
        </div>
      <?php endforeach; ?>
    </div>
    <div class="bulkbar">
      <span>With ticked rows:</span>
      <select name="bulk">
        <option value="">Choose an action…</option>
        <optgroup label="Change status"><?php foreach ($statuses as $s): ?><option value="status:<?= h($s) ?>"><?= h($s) ?></option><?php endforeach; ?></optgroup>
        <optgroup label="Assign to"><?php foreach (users() as $id => $name): ?><option value="assign:<?= $id ?>"><?= h($name) ?></option><?php endforeach; ?><option value="assign:none">Nobody</option></optgroup>
        <optgroup label="Delete"><option value="delete">Delete permanently</option></optgroup>
      </select>
      <label class="check"><input type="checkbox" name="confirm" value="yes"> Yes, delete (only needed for Delete)</label>
      <button class="btn ghost">Apply to ticked</button>
    </div>
  </form>
  <p class="pager">
    <span><?= $total ?> total</span>
    <?php if ($page > 1): ?><a href="<?= h(link_with($params, ['status' => $f['status'], 'page' => $page - 1])) ?>">&larr; Previous</a><?php endif; ?>
    <?php if ($total > $per): ?><span>Page <?= $page ?> of <?= (int) ceil($total / $per) ?></span><?php endif; ?>
    <?php if ($page * $per < $total): ?><a href="<?= h(link_with($params, ['status' => $f['status'], 'page' => $page + 1])) ?>">Next &rarr;</a><?php endif; ?>
  </p>
<?php endif;
bottom();
