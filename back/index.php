<?php 
include("db.php"); //include tira el codi de l'arxiu que dius, aquest obre la db


if(isset($_GET['nom']) && isset($_GET['preu'])) { // si s'ha enviat el nom i preu del producte: 
    #POST envia dades en el cos de la solicitud http. Per enviar dades ocultes 
    #GET envia dades adjuntes al url com a paràmetres. http://localhost:8080/phpProject/back/index.php?nom=Joel 
    $nom = $_GET['nom']; // obtener el nombre del producto
    $preu = $_GET['preu']; // obtener el precio del producto
    
    // realizar la consulta para añadir el producto a la base de datos
    $consulta = "INSERT INTO productes (nom, preu) VALUES ('$nom', '$preu')";  #com fer una consulta d'insertar dades en mysql
    $resultado = mysqli_query($conn, $consulta);  #executa la consulta $consulta a la db $conn

    
    // enviar el nom y el preu del producto afegit com a resposta json
    $producto_array = array("nom" => $nom, "preu" => $preu);
    echo json_encode($producto_array);
} else {
        // enviar un meissatge d'error com a resposta
        echo "Error al añadir el producto";
}
?>
