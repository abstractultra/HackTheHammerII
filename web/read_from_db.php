<?php
require "connect_to_db.php";

$data = $db->query("select * from users");

$query_result = [];

while ($row = $data->fetch_array()) {
    //$sleep_score = $row['sleep_score'];
    $query_result[$row['user_id']] = $query_result[$sleep_score];
    //$query_result[] = $row;
    //echo ($row['sleep_score']);
}
$json_data = json_encode($query_result);

echo $json_data;