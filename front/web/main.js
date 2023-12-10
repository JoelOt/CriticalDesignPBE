var password = null;  //es global

document.addEventListener("DOMContentLoaded", function () {  //amaguem la pag principal al iniciar
    document.getElementById("mainPage").style.display = "none";
});

function logout() {  //logout amaga la mainPage i mostra la loginPage
    document.getElementById("mainPage").style.display = "none";
    document.getElementById("loginPage").style.display = "block";
    console.log("LOGOUT")
}

function temporizador() {
    console.log("timeout")
    temp = setTimeout(function () { //Timeout
        var logoutButton = document.getElementById('logoutButton');
        logoutButton.click(); // Simula un clic
    }, 20000); //en ms. 
    return temp;
}

function login() {  //agafem user i contrasenya
    var userName = document.getElementById("userName").value;
    password = document.getElementById("password").value;
    var constraints = `students?userName=${userName}&password=${password}`;  //aix ho haurem de concatenar a la request
    console.log("Login: " + constraints);
    AJAX(constraints, function(result){ //fem una request per validar les credencials,   [{ res: true }] per fer proves sense server;
        console.log(result);
        if (result[0].res) { //res=nom que volguem posar al que retorna el php
            document.getElementById("loginPage").style.display = "none"; //amaguem el login
            document.getElementById("mainPage").style.display = "block";  //mostrem la mainPage
            document.getElementById("usernameDisplay").innerText = userName;  //passem el UserName per mostrar-lo a usernameDisplay
            temp = temporizador();
    
        }else {  //si es fals, ho avisem en pop-up
            alert("Credencials incorrectes, Escriu be!");
        }
    });
}

function request() {
    clearTimeout(temp);  //fem reset al timeout
    console.log("reset timeout")
    temp = temporizador();
    var constraints = document.getElementById("consulta").value; // + `&id=${password}`;
    console.log("Consulta: " + constraints)
    AJAX(constraints, function(result) {  //es fa la solicitud i es guarda el resultat en la funció de callback. 
        console.log(result);    //descripció de callback: es fa quan rep result
        llenarTabla(result);
    });
}

function llenarTabla(result) {  //omplim la taula de l'html amb les dades de result, sra una arrayList
    var tbody = document.getElementById("tablaBody");  // Obtenim el cos de la taula
    tbody.innerHTML = ""; // Netejem la taula
    for (var item of result) { //cada item: {"day":"Tue ","hour":"08:00:00.000000","subject":"AST","room":"A4001"}
        var row = document.createElement('tr');  //afegim el nombre de columnes pertinents
        for (var key in item) {  //anem agafant cada valor dintre el item i afegim una cela amb aquest
            var cell = document.createElement('td');
            cell.textContent = item[key];
            row.appendChild(cell);
        }
        tablaBody.appendChild(row);
    }
}

function AJAX(constraints, callback) {
    var xhr = new XMLHttpRequest(); // Crea un objeto XMLHttpRequest
    xhr.open("GET", `http://localhost:8080/CriticalDesignPBE/back/index.php/${constraints}`); // Configura la solicitud
    //xhr.setRequestHeader("id", `${password}`);
    xhr.onload = function () {  //si te status 200 (o<300)
        if (xhr.status == 200) {
            var result = JSON.parse(xhr.responseText);  // Convierte la respuesta JSON a un objeto JavaScript
            callback(result);  // Llama al callback con el resultado
        } else {
            console.error("Error en la solicitud AJAX:", xhr.statusText);
        }
    };
    xhr.onerror = function () { // Maneja errores de red
        console.error("Error de red en la solicitud AJAX");
    };
    xhr.send(); // Envía la solicitud
    return true;
}