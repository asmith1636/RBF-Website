<?php
// Settings for the RBF admin (rbfconstruction.com/admin).
//
// Copy this into a file named rbf-config.php in the folder ABOVE public_html on Hostinger
// (File Manager: domains/rbfconstruction.com/rbf-config.php), then fill in the values.
// Never put the real file in GitHub or inside public_html.
return [
    // hPanel > Databases > MySQL Databases
    'db_host' => 'localhost',
    'db_name' => 'u000000000_rbf',
    'db_user' => 'u000000000_rbf',
    'db_pass' => 'the database password you chose',

    // Make up a long phrase (12+ characters). You type it once at /admin/setup.php to create the
    // first login, so nobody else can claim the admin before you do.
    'setup_key' => 'make up a long phrase here',
];
