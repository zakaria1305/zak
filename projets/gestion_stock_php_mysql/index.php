<?php
$conn = new mysqli('localhost', 'root', '', 'stock_db');
if ($conn->connect_error) die('Erreur de connexion');

$sql = 'SELECT * FROM produits';
$result = $conn->query($sql);

while ($row = $result->fetch_assoc()) {
    echo $row['nom'] . ' - ' . $row['prix'] . '€<br>';
}
?>