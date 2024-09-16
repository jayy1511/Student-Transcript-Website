// Database/db.php
<?php
$servername = "localhost";
$username = "root";
$password = "Jay@1101";
$dbname = "database_";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
