<?php 
session.start();
include("db.php"); //include tira el codi de l'arxiu que dius, aquest obre la db

if(isset($_GET['uid'])){
    $uidGet = $_GET['uid'];
    $_SESSION['uid'] = $uidGet;  //session es per mantenir el valor en diferents requests
    $consultaUid = SELECT userName FROM students WHERE uid = '$uidGet'";
    $userName = mysqli_query($conn,         
$consultaUid);        
    //echo "userName:" . $userName;  //enviem el userName per ensenyar-lo per LCD
} 
   
if(isset($_GET['request'])){ // si s'ha enviat una request (timetables, marks o tasks):
 $request = $_GET['request'];
    if($request == 'timetables'){
        $consulta = "SELECT * FROM timetables";
        if(isset($_GET['day'])){
            $day = $_GET['day'];
            $consulta .= " WHERE day = '$day'";
            if(isset($_GET['hour'])){
                $hour = $_GET['hour'];
                $consulta .= " AND hour = '$hour'";
            }
        }if(isset($_GET['limit'])){
            $limit = $_GET['limit'];
            $consulta .= " LIMIT $limit"; 
        }

    }elseif($request == 'marks'){
        $uid = $_SESSION['uid'];  //reagafem el valor uid de la sessió     
        $consulta = "SELECT * FROM marks WHERE uid = '$uid'";
        if(isset($_GET['subject'])){
            $subject = $_GET['subject'];
            $consulta .= " AND subject = '$subject'";
        }if(isset($_GET['mark[lt]'])){
       s     $mark = $_GET['mark[lt]'];
            $consulta .= " AND mark < '$mark'";
}

    }elseif($request == 'tasks'){
        $consulta = "SELECT * FROM tasks ORDER BY date";
        if(isset($_GET['date'])){
            $date = $_GET['date'];
            $consulta .= " WHERE date = '$date'";
        }
        if(isset($_GET['limit'])){
            $limit = $_GET['limit'];
            $consulta .= " LIMIT $limit"; 
        }
    }
    $resultat = mysqli_query($conn, $consulta);  //executa la consulta $consulta a la db $conn
    $data= array();
    while($row = mysqli_fetch_assoc($resultat)){
        $data[] = $row;
    }
    header('Content-Type: application/json');
    echo json_encode($data);
}
?>
