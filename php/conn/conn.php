<?php
$host = "localhost:3308";
$usuario = "root";
$senha = "";
$bd = "database";

$conn = new mysqli($host, $usuario, $senha, $bd);

if($conn->connect_errno)
    echo "Falha na conexão: (".$conn->connect_errno.") ".$conn->connect_error;

$sql = "SELECT * FROM tabel";
$result = mysqli_query($conn, $sql);
$json_array = array();

while($row = mysqli_fetch_assoc($result))
{
    $json_array[] = $row;
}




?>

