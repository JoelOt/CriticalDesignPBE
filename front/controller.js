document.addEventListener("DOMContentLoaded", function () {  //amaguem la pag principal al iniciar
    document.getElementById("mainPage").style.display = "none";
});

function login() {  //agafem user i contrasenya
    var userName = document.getElementById("userName").value;
    var passWord = document.getElementById("passWord").value;

    if (validarCredencialesEnElServidor(userName, passWord)) {  //verifiquem credencials, si es True:
        document.getElementById("loginPage").style.display = "none"; //amaguem el login
        document.getElementById("mainPage").style.display = "block";  //mostrem la mainPage
        document.getElementById("usernameDisplay").innerText = userName;  //passem el UserName per mostrar-lo a usernameDisplay
    } else {  //si es fals, ho avisem a terminal
        alert("Credenciales incorrectas. Inténtalo de nuevo.");
    }
}

function validarCredencialesEnElServidor(userName, passWord) {  //el php retorna true si coincideixen amb les de la db i fals en cas contrari
    //if (credencialesValidas) {
        return realizarSolicitudAJAX(userName, passWord);  //s'ha de fer una llogica, el return com a tal aqui no

    //} else {
      //  alert("Credenciales incorrectas. Inténtalo de nuevo.");
//}
}

function realizarSolicitudAJAX(username, passWord){  //fer solicitud, hauria de ser genèric

    return true;
    fetch("http://localhost:8080/CriticalDesignPBE/back/index.php", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
            // Puedes agregar más encabezados si es necesario
        }
    })
    .then(response => {  
        // Verifica si la respuesta es exitosa (código de estado 200)
        if (!response.ok) {
            throw new Error(`Error en la solicitud AJAX: ${response.status} - ${response.statusText}`);
        }
        // Devuelve la respuesta en formato JSON
        return response.json();
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