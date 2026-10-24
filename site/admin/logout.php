<?php
define('RBF', true);
require __DIR__ . '/_lib/boot.php';

admin_headers();
check_csrf();
end_session();
redirect('login.php');
