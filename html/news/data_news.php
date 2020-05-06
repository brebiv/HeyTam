<?php

require_once 'classes_news.php';
#$news = array();

#$con = mysqli_connect('localhost', 'root', '', 'heytam');
#if (mysqli_connect_errno()){
#    echo "Failed to connect to MySQL ". mysqli_connect_error();
#}

#$query = "SELECT * FROM news";
#$result = mysqli_query($con, $query);

#while ($row = mysqli_fetch_array($result)){
#    $news[] = new Article($row);
#}

class MyDB extends SQLite3 {
	function __construct() {
		$this->open('../db.sqlite3');
	}
}

function get_articles(){
	$db = new MyDB();
	$articles = array();
	$result = $db->query("SELECT * FROM news");
	while($row = $result->fetchArray(SQLITE3_ASSOC)) {
		#echo $row['title'];
		$articles[] = new Article($row);
	}
	return array_reverse($articles);
}
