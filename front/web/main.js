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
    var constraits = `students?userName=${userName}&password=${password}`;  //aix ho haurem de concatenar a la request
    console.log("Login: " + constraits);

    var result = AJAX(constraits);  //fem una request per validar les credencials,   [{ res: true }] per fer proves sense server; 
    if (result[0].res) { //res=nom que volguem posar al que retorna el php
        document.getElementById("loginPage").style.display = "none"; //amaguem el login
        document.getElementById("mainPage").style.display = "block";  //mostrem la mainPage
        document.getElementById("usernameDisplay").innerText = userName;  //passem el UserName per mostrar-lo a usernameDisplay
        temp = temporizador();

    } else {  //si es fals, ho avisem en pop-up
        alert("Credencials incorrectes, Escriu be!");
    }
}

function request() {
    clearTimeout(temp);  //fem reset al timeout
    console.log("reset timeout")
    temp = temporizador();
    var constraits = document.getElementById("consulta").value + `&id=${password}`;
    console.log("Consulta: " + constraits)
    var result = AJAX(constraits);
    /*var result = [
        { id: 1, nombre: 'Ejemplo 1', descripcion: 'Descripción 1' },
        { id: 2, nombre: 'Ejemplo 2', descripcion: 'Descripción 2' },
        { id: 3, nombre: 'Ejemplo 3', descripcion: 'Descripción 3' }
    ];*/
    llenarTabla(result);
}

function llenarTabla(result) {
    console.log(result);

    var tbody = document.getElementById("tablaBody");  // Obtener el cuerpo de la tabla
    tbody.innerHTML = ""; // Limpiar cualquier contenido existente en la tabla

    for (var item of result) { //cada item: { id: 1, nombre: 'Ejemplo 1', descripcion: 'Descripción 1' }
        var row = document.createElement('tr');  //afegim el nombre de columnes pertinents

        for (var key in item) {
            var cell = document.createElement('td');
            cell.textContent = item[key];
            row.appendChild(cell);
        }
        tablaBody.appendChild(row);
    }
}

function AJAX(constraits) {
    var xhr = new XMLHttpRequest(); // Crea un objeto XMLHttpRequest
    xhr.open("GET", `http://localhost:8080/CriticalDesignPBE/back/index.php/${constraits}`); // Configura la solicitud
    //xhr.setRequestHeader("id", `${password}`);
    xhr.onload = function () {  //si te status 200 (o<300)
        if (xhr.status == 200) {
            var result = JSON.parse(xhr.responseText);  // Converteix la resposta JSON a un objecte JavaScript
            return result;
        } else {
            console.error("Error en la solicitud AJAX:", xhr.statusText);
        }
    };
    xhr.onerror = function () { // Maneja errores de red
        console.error("Error de red en la solicitud AJAX");
    };
    xhr.send(); // Envía la solicitud

    return true; // Devuelve true para este ejemplo básico
}

/*
function AJAX(constraits){  //fer solicitud, hauria de ser genèric

    fetch("http://localhost:8080/CriticalDesignPBE/back/index.php")   //url de la solicitud (es get implícitament)
        .then(response => {  
            if (!response.ok) { // Verifica si la respuesta es exitosa (código de estado 200)
                throw new Error(`Error en la solicitud AJAX: ${response.status} - ${response.statusText}`);
            }
            return response.json(); // Devuelve la respuesta en formato JSON
     })
     .then(result => {
        // Maneja la respuesta exitosa del servidor
        console.log("Respuesta del servidor:", result);

        // Puedes realizar operaciones con los datos recibidos aquí
    })
    .catch(error => {
        console.error("Error en la solicitud AJAX:", error);
    });

    return true; // Devuelve true para este ejemplo básico
}
*/