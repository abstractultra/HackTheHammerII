<?php
$db = new mysqli('localhost:3306', 'dbaccess', 'HzhoI4iTNLQ5Le8e', 'hackhammer');

$db->query("create table if not exists users (user_id int, sleep_score int)");