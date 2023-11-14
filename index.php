<?php 
include("db.php"); //include tira el codi de l'arxiu que dius, aquest obre la db

if(isset($_GET['request'])){ // si s'ha enviat el timetables:
    $request = $_GET['request'];  //pot ser timetables, tasks, marks
    if($request == 'timetables'){   //falta el limit
        $consulta = "SELECT * FROM timetables";
        if(isset($_GET['day'])){ //si es timetables hem de mirar si ha especificat day i hour
            $day = $_GET['day'];
            $consulta .= " WHERE day = '$day'";  //afegim a la consulta el filtre de dia
            if(isset($_GET['hour'])){
                $hour = $_GET['hour'];
                $consulta .= "AND hour = '$hour'";
            }
        }elseif(isset($_GET['limit'])){
            $limit = $_GET['limit'];
            $consulta .= " LIMIT $limit"; 
        }
    }

    if($request == 'marks'){  //a fer
        $consulta = "SELECT subject FROM marks";
    }
    if($request == 'tasks'){  //a fer
        $consulta = "SELECT * FROM tasks";
    }

    $resultat = mysqli_query($conn, $consulta);  #executa la consulta $consulta a la db $conn
    $data= array();
    while($row = mysqli_fetch_assoc($resultat)){
        $data[] = $row;
    }
    header('Content-Type: application/json');
    echo json_encode($data);
}
?>
