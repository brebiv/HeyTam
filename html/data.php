<?php

require_once 'classes.php';

class MyDB extends SQLite3 {
	function __construct() {
		$this->open('db.sqlite3');
	}
}
$quotes = array();

$db = new MyDB();
if (!$db){
    echo "Failed to connect to Database";
}

$query = "SELECT * FROM quotes";
$result = $db->query($query);

while ($row = $result->fetchArray(SQLITE3_ASSOC)){
    $quotes[] = new Quote($row);
}
