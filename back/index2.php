<?php
include("db.php"); //include aplica el codi de l'arxiu que dius, aquest obre la db

//https://localhost:8080/CriticalDesignPBE/back/index.php/timetables?day=FRi&hour=8:00&subject=PBE 

function parse_query($query){   //fa una llista key-value separant per =
    foreach($query as $val){
        list($key, $value) = explode('=', $val);
        $params[$key] = $value;
    }
    return $params;
}
$table = ltrim($_SERVER['PATH_INFO'], '/'); //s'ha de treure el '/' devant de la taula
$consulta = "SELECT * FROM {$table}";  
if($_SERVER['QUERY_STRING']!= NULL){
    $query = explode('&', $_SERVER['QUERY_STRING']); //quedarà un array [day=Fri, hour=8:00, subject=PBE]

    $params = parse_query($query);  //Array ( [day] => FRi, [hour] => 8:00, [subject] => PBE )
    $primeraCondicio = true;
    foreach($params as $key => $value){
        if(isset($key)){
            $consulta .= ($primeraCondicio ? " WHERE" : " AND");  //tria WHERE si &primeraciondició=True
            $primeraCondicio = false;  
 
            $keyParts = explode('[', $key);     //en aquesta secció de codi es on posem les codicións lt and gt
            if (isset($keyParts[1])) {
                $cond = trim($keyParts[1],']');
                $key0 = $keyParts[0];
                if($cond =='gt'){
                    $consulta .=" $key0 > '$value'";
                }else if ($cond =='lt'){
                    $consulta .=" $key0 < '$value'";
                }                               //si volem posar mes condicionants només hem d'afegir else if
            }else{
                $consulta .=" $key = '$value'";

            }
        }
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
