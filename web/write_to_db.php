<?php
require "connect_to_db.php";

if ($_SERVER['REQUEST_METHOD'] == "POST");
$db->query("insert into users values ({$_POST['user_id']}, {$_POST['sleep_score']})");