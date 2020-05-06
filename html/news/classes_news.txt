<?php

require_once 'classes_news.php';
$news = array();

$con = mysqli_connect('localhost', 'root', '', 'heytam');
if (mysqli_connect_errno()){
    echo "Failed to connect to MySQL ". mysqli_connect_error();
}

$query = "SELECT * FROM news";
$result = mysqli_query($con, $query);

while ($row = mysqli_fetch_array($result)){
    $news[] = new Article($row);
}