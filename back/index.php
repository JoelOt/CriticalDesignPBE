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
$limit = NULL;
if($_SERVER['QUERY_STRING']!= NULL){
    $query = explode('&', $_SERVER['QUERY_STRING']); //quedarà un array [day=Fri, hour=8:00, subject=PBE]

    $params = parse_query($query);  //Array ( [day] => FRi, [hour] => 8:00, [subject] => PBE )
    $primeraCondicio = true;
    foreach($params as $key => $value){
        if(isset($key)){
            if($key !="limit"){
                $consulta .= ($primeraCondicio ? " WHERE" : " AND");  //tria WHERE si &primeraciondició=True
                $primeraCondicio = false;  
 
                $keyParts = explode('[', $key);     //en aquesta secció de codi es on posem les codicións lt and gt
                $simb ='=';
                if (isset($keyParts[1])) {
                    $cond = trim($keyParts[1],']');
                    if($cond =='gt'){
                        $simb ='>';
                    }else if ($cond =='lt'){
                        $simb ='<';
                    }else if ($cond =='gte'){
                        $simb = '>=';
                    }else if ($cond =='lte'){
                        $simb = '<=';
                    }
                    //si volem posar mes condicionants només hem d'afegir else if
                }
                $key = $keyParts[0];
                if($key=="date" && $value = "now"){
                    $value = "CURRENT_DATE";
                }
                $consulta .=" $key $simb '$value'";

            }else if($key =="limit"){
                $limit=$value;
            }
        }
    }
}
if ($table == 'timetables'){
    $consulta .=" ORDER BY FIELD(day, 'Mon', 'Tue', 'Wen', 'Thu', 'Fri'),hour ASC";
}else if($table == 'tasks'){
    $consulta .=" ORDER BY date ASC";
}else if ($table == 'marks'){
    $consulta .=" ORDER BY mark ASC";
}
//afegir orders si es necesari
if ($limit != NULL){
    $consulta .=" LIMIT $limit";

}


$result = mysqli_query($conn, $consulta);  //executa la consulta $consulta a la db $conn
$data= array(); //l'inicialitzem com un array buit
while($row = mysqli_fetch_assoc($result)){  //anem recollint els arrays de les diferents columnes i fent un array de arrays, és a dir, una matriu
    $data[] = $row;
}
header('Content-Type: application/json');  //indiquem a la capçalera que les dades son en foramt json
echo json_encode($data);    //les enviem al client codificades en aquest format
?>
