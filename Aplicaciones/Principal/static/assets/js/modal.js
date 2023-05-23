function newPerson(tipo) {
  $("#newUser").modal("show");
  if (tipo == 'editar') {
    $('#nuevouser').html('modal editar persona');
    $('#titulo').html('Editar usuario');
    $('#codigo').val('1');
    $('#nombre').val('Herman');
    $('#identificacion').val('');
    $('#direccion').val('');
    $('#telefono').val('');
    $('#usuario').val('');
    $('#contraseña').val('');
    $('#correo').val('');
    $('#nacimiento').val('');
    $('#add').html('Guardar');
  }
  else {
    $('#nuevouser').html('modal nueva persona');
    $('#titulo').html('Nuevo usuario');
    $('#codigo').val('');
    $('#nombre').val('');
    $('#identificacion').val('');
    $('#direccion').val('');
    $('#telefono').val('');
    $('#usuario').val('');
    $('#contraseña').val('');
    $('#correo').val('');
    $('#nacimiento').val('');
    $('#add').html('Agregar')
  }

}

function newProduct(tipo) {
  $("#newProd").modal("show");
  if (tipo == 'edita'){
    $('#mensajeprod').html('modal editar producto');
    $('#titulo').html('Editar Producto');
    $('#codigo').val('1');
    $('#producto').val('Papas Fritas');
    $('#stock').val('35');
    $('#precio').val('3.500');
    $('#add').html('Guardar');
  }
  else{
    $('#mensajeprod').html('modal nuevo producto')
    $('#titulo').html('Nuevo Producto')
    $('#codigo').val('')
    $('#nombre').val('')
    $('#stock').val('')
    $('#precio').val('')
    $('#add').html('Agregar')

  }
}


function newProoved(tipo) {
  $("#newProov").modal("show");
  if (tipo == 'edit'){
    $('#nuevoprov').html('modal editar proveedor');
    $('#titulo').html('Editar Proveedor')
    $('#codigo').val('1')
    $('#proveedor').val('')
    $('#correo').val('')
    $('#direccion').val('')
    $('#telefono').val('')
    $('#add').html('Guardar')
  }
  else{
    $('#nuevprov').html('modal nuevo proovedor')
    $('#titulo').html('Nuevo Proveedor')
    $('#codigo').val('')
    $('#proveedor').val('')
    $('#correo').val('')
    $('#direccion').val('')
    $('#telefono').val('')
    $('#add').html('Agregar')
  }
}
