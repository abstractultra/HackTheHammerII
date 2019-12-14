<?php
require "connect_to_db.php";

$data = $db->query("select * from users");

$json_data = json_encode($data->fetch_assoc());

echo $json_data;