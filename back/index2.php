<?php
include("db.php"); //include aplica el codi de l'arxiu que dius, aquest obre la db

//https://localhost:8080/CriticalDesignPBE/back/index.php/timetables?day=FRi&hour=8:00&subect=PBE 

function parse_query($query){   
    foreach($query as $val){
        list($key, $value) = explode('=', $val);
        $params[$key] = $value;
    }
    return $params;
}
$table = $_SERVER['PATH_INFO'];
$query = explode('&', $_SERVER['QUERY_STRING']); //quedarà un array [day=Fri, hour=8:00, subject=PBE]
$params = parse_query($query);  //Array ( [day] => FRi, [hour] => 8:00, [subject] => PBE )

$consulta = "SELECT * FROM '$table'";
$primeraCondicio = true;
foreach($params as $key => $value){
    if(isset($key)){
        $consulta .= ($primeraCondicio ? " WHERE" : " AND")
        $primeraCondicio = false;
        
        $consulta .=" '$key' = '$value'";
    }
}

$result = mysqli_query($conn, $consulta);  //executa la consulta $consulta a la db $conn
$data= array(); //l'inicialitzem com un array buit
while($row = mysqli_fetch_assoc($result)){  //anem recollint els arrays de les diferents columnes i fent un array de arrays, és a dir, una matriu
    $data[] = $row;
}
header('Content-Type: application/json');  //indiquem a la capçalera que les dades son en foramt json
echo json_encode($data);    //les enviem al client codificades en aquest format
?>

