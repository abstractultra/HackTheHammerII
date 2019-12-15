<?php
require "connect_to_db.php";

$data = $db->query("select * from users");

$query_result = [];

while ($row = $data->fetch_array()) {
    $query_result[$row['user_id']] = $row['sleep_score'];
}
$json_data = json_encode($query_result);

echo $json_data;