$(document).ready(function () {    
  $(".infoContainer").load("../templates/inicio.html");
  $(".miga").html("Inicio");  
});

function menu(parametro) {    
  if (parametro == 0) {
    $(".infoContainer").load("../templates/inicio.html");
    $(".miga").html("Inicio");
  } else if (parametro == 1) {
    $(".infoContainer").load("../templates/personal.html");
    $(".miga").html("Personal");
  } else if (parametro == 2) {
    $(".infoContainer").load("../templates/Productos.html");
    $(".miga").html("Productos");
  } else if (parametro == 3) {
    $(".infoContainer").load("../templates/Proveedores.html");
    $(".miga").html("Proveedores");
  } else if (parametro == 4) {
    $(".infoContainer").load("../templates/Pedidos.html");
    $(".miga").html("Pedidos");
  } else if (parametro == 5) {
    $(".infoContainer").load("../templates/Facturar.html");
    $(".miga").html("Facturar");
  } else if (parametro == 6) {
    $(".infoContainer").load("../templates/login.html");
    $(".miga").html("Exit");
  }
}