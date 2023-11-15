<?php 
include("db.php"); //include tira el codi de l'arxiu que dius, aquest obre la db

if(isset($_GET['uid'])){
    $uid = $_GET['uid'];
    $consUid = SELECT nom FROM students WHERE uid = '$uid'";
   $userName = mysqli_query($conn,         
$consUid);        
    echo "userName:" . $userName;
    
if(isset($_GET['request'])){ // si s'ha enviat el una request (timetables, marks o tasks):
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
$consulta = "SELECT * FROM marks WHERE uid = '$uid'";
        if(isset($_GET['subject'])){
            $subject = $_GET['subject'];
            $consulta .= " AND subject = '$subject'";
        }if(isset($_GET['mark[lt]'])){
            $mark = $_GET['mark[lt]'];
            $consulta .= " AND mark < '$mark'";
}

    }elseif($request == 'tasks'){
        $consulta = "SELECT * FROM tasks";
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
