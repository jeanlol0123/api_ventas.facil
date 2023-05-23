$(document).ready(function () {    
  $(".infoContainer").load("/inicio/");
  $(".miga").html("Inicio");  
});

function menu(parametro) {    
  if (parametro == 0) {
    $(".infoContainer").load("/inicio/");
    $(".miga").html("Inicio");
  } else if (parametro == 1) {
    $(".infoContainer").load("/personal/");
    $(".miga").html("Personal");
  } else if (parametro == 2) {
    $(".infoContainer").load("/producto/");
    $(".miga").html("Productos");
  } else if (parametro == 3) {
    $(".infoContainer").load("/proveedores/");
    $(".miga").html("Proveedores");
  } else if (parametro == 4) {
    $(".infoContainer").load("/pedidos/");
    $(".miga").html("Pedidos");
  } else if (parametro == 5) {
    $(".infoContainer").load("/facturas/  ");
    $(".miga").html("Facturar");
  } else if (parametro == 6) {
    $(".infoContainer").load("login/");
    $(".miga").html("Exit");
  }
}


