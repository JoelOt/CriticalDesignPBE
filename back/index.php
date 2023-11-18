<?php 
//session_start();
include("db.php"); //include tira el codi de l'arxiu que dius, aquest obre la db

//if(isset($_GET['uid'])){
//    $uidGet = $_GET['uid'];
//    $_SESSION['uid'] = $uidGet;  //session es per mantenir el valor en diferents requests
//    $consultaUid = SELECT userName FROM students WHERE uid = '$uidGet'";
//    $resUid = mysqli_query($conn,$consultaUid);
//    $userName = mysqli_fetch_assoc($resultUid)['userName'];        
    //echo "userName:" . $userName;  //enviem el userName per ensenyar-lo per LCD
//} 
$requestUri = $_SERVER['REQUEST_URI'];
$parts = explode('/', $requestUri);
$parts = array_filter($parts);
$parts = end($parts);
$parts = explode('?', $parts);
$route = $parts[0];

switch ($route) {
    case 'timetables':
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
        break;

    case 'marks':     
        $consulta = "SELECT * FROM marks";
        if(isset($_GET['subject'])){
            $subject = $_GET['subject'];
            $consulta .= " WHERE subject = '$subject'";
        }if(isset($_GET['mark[lt]'])){
            $mark = $_GET['mark[lt]'];
            $consulta .= " AND mark < '$mark'";
        }
        break;

    case 'tasks':
        $consulta = "SELECT * FROM tasks ORDER BY date";
        if(isset($_GET['date'])){
            $date = $_GET['date'];
            $consulta .= " WHERE date = '$date'";
        }
        if(isset($_GET['limit'])){
            $limit = $_GET['limit'];
            $consulta .= " LIMIT $limit"; 
        }
        break;
    default:
        break;
    }
    $resultat = mysqli_query($conn, $consulta);  //executa la consulta $consulta a la db $conn
    $data= array();
    while($row = mysqli_fetch_assoc($resultat)){
        $data[] = $row;
    }
    header('Content-Type: application/json');
    echo json_encode($data);
?>
