var password = null;
var title = null;

document.addEventListener("DOMContentLoaded", function () {  //amaguem la pag principal al iniciar
    document.getElementById("mainPage").style.display = "none";
});

function logout() {  //logout amaga la mainPage i mostra la loginPage
    document.getElementById("mainPage").style.display = "none";
    document.getElementById("loginPage").style.display = "block";
    document.getElementById("tabla").style.display = "none";
    console.log("LOGOUT")
}

function temporizador() {
    console.log("timeout")
    temp = setTimeout(function () { //Timeout
        var logoutButton = document.getElementById('logoutButton');
        logoutButton.click(); // Simula un clic
    }, 200000); //en ms. 
    return temp;
}

function login() {  //agafem user i contrasenya
    var userName = document.getElementById("userName").value;
    password = document.getElementById("password").value;
    var constraints = `students?userName=${userName}&uid=${password}`;  //aix ho haurem de concatenar a la request
    console.log("Login: " + constraints);
    AJAX(constraints, function (result) { //fem una request per validar les credencials,   [{ res: true }] per fer proves sense server;
        console.log(result);
        try {  //try-catch per tal de que si result[0] està buit no peti la web i salti la alerta
            if (result[0].userName == userName) {
                document.getElementById("loginPage").style.display = "none"; //amaguem el login
                document.getElementById("mainPage").style.display = "block";  //mostrem la mainPage
                document.getElementById("usernameDisplay").innerText = userName;  //passem el UserName per mostrar-lo a usernameDisplay
                temp = temporizador();

            } else {  //passa si per algun motiu existeix l'usuari pero coincideixen (estan girats a la db o algo)
                alert("Credencials incorrectes, Escriu be!");  
            }
        } catch {
            alert("Credencials incorrectes, Escriu be!");
        }
    });
}

function request() {
    clearTimeout(temp);  //fem reset al timeout
    console.log("reset timeout")
    temp = temporizador();
    var constraints = document.getElementById("consulta").value;  //timetables
    var partes = constraints.split("?");
    title = partes[0];
    if (title == "marks") {  //nomes enviem el uid si demanem per marks i valorant si hi ha condicions
        if (partes.length == 1) {
            constraints = partes[0] + "?" + "id=" + `${password}`;
        } else {
            constraints = constraints + "&" + "id=" + `${password}`;
        }
    }
    console.log("Consulta: " + constraints)
    AJAX(constraints, function (result) {  //es fa la solicitud i es guarda el resultat en la funció de callback. 
        console.log(result);    //descripció de callback: es fa quan rep result, mola poder-la definir directament aqui :)
        omplirTabla(result);
    });
}

function omplirTabla(result) {  //omplim la taula de l'html amb les dades de result, sra una arrayList
    document.getElementById("tabla").style.display = "table";
    var tbody = document.getElementById("tablaBody");  // Obtenim el cos de la taula
    tbody.innerHTML = ""; // Netejem la taula

    var caption = document.querySelector("#tabla caption");  //serveix per netejar el caption de al request anterior
    if (caption) {
        tabla.removeChild(caption);
    }

    caption = document.createElement('caption');    //títol de la taula
    caption.textContent = title;
    tabla.appendChild(caption);

    var headerRow = document.createElement('tr');   //capçalera de les columnes
    for (var key in result[0]) {
        var headerCell = document.createElement('th');
        headerCell.textContent = key;
        headerRow.appendChild(headerCell);
    }
    tbody.appendChild(headerRow);

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
    var xhr = new XMLHttpRequest(); // Crea un objecte XMLHttpRequest
    xhr.open("GET", `http://localhost:8080/CriticalDesignPBE/back/index2.php/${constraints}`); // Configura la solicitud
    xhr.onload = function () {  //si te status 200
        if (xhr.status == 200) {
            var result = JSON.parse(xhr.responseText);  // Convertim la resposta JSON a un objete JavaScript
            callback(result);  // Cridem a la finció de callback 
        } else {
            console.error("Error en la solicitud AJAX:", xhr.statusText);
        }
    };
    xhr.onerror = function () { // si hi ha errors en la red
        console.error("Error de red en la solicitud AJAX");
    };
    xhr.send(); // Envía la solicitud
    return true; 
}
