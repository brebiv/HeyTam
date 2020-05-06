<?php
foreach (getallheaders() as $name => $value){
	echo "$name: $value<br>";
}

$ipAddress = $_SERVER['REMOTE_ADDR'];
if (array_key_exists('HTTP_X_FORWARDED_FOR', $_SERVER)) {
	$ipAddress = array_pop(explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']));
	echo "Very funny, your proxy told me who are you :)";
}
echo "<br><br><br>";
echo "Hah, your address is -> $ipAddress";

?>
