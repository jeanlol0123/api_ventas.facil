from django.shortcuts import render, redirect
from .models import Usuarios,Producto,Proveedore
from django.http.response import JsonResponse
from rest_framework import viewsets
from .serializer import UsuariosSerializer,ProductoSerializer,ProveedoreSerializer
from django.urls import reverse

# Create your views here.

#API BY jeanlol
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedore.objects.all()
    serializer_class = ProveedoreSerializer



def index(request):
    return render(request, "index.html")
#Registrar las vistas del menu desplegable de la derecha
###############################################################################################################################
def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'inicio.html')

def personal(request):
    return render(request, 'personal.html')

def productos(request):
    return render(request, 'Productos.html')

def proveedores(request):
    return render(request, 'Proveedores.html')

def pedidos(request):
    return render(request, 'Pedidos.html')

def facturas(request):
    return render(request, 'Facturar.html')

def login(request):
    return render(request, 'Login.html')
###############################################################################################################################
#VISTAS DE USUARIOS
# def registrarUsuario(request):
#     tCodigo = request.POST['codigo']
#     tNombre = request.POST['nombre']
#     tIdentificacion = request.POST['identificacion']
#     tDireccion = request.POST['direccion']
#     tTelefono = request.POST['telefono']
#     tUsuario = request.POST['usuario']
#     tCorreo = request.POST['correo']
#     tNacimiento = request.POST['nacimiento']
#     tGenero = request.POST['genero']
#     tUser = request.POST['tipouser']

#     usuario = Usuarios.objects.create(codigo=tCodigo, nombre=tNombre, identificacion=tIdentificacion, direccion=tDireccion, telefono=tTelefono ,usuario=tUsuario,correo=tCorreo, nacimiento=tNacimiento, genero=tGenero, tipouser=tUser        
#     )
#     return redirect('/personal/')

#recuperar los archivos en json para mostrar en datatable
def verUsuarios(request):
    usuarios=list(Usuarios.objects.values())
    data={'usuarios':usuarios}
    return JsonResponse(data)

def verProductos(request):
    productos=list(Producto.objects.values())
    data={'productos':productos}
    return JsonResponse(data)

def verProveedores(request):
    proveedores=list(Proveedore.objects.values())
    data={'proveedores':proveedores}
    return JsonResponse(data)

#Views de Personal
def registrarUsuario(request):
    tableCodigo = request.POST['codigo']
    tableNombre = request.POST['nombre']
    tableIdentificacion = request.POST['identificacion']
    tableDireccion = request.POST['direccion']
    tableTelofono = request.POST['telefono']
    tableUsuario = request.POST['usuario']
    tableContrasena = request.POST['contrasena']
    tableCorreo = request.POST['correo']
    tableNacimiento = request.POST['nacimiento']
    tableGenero = request.POST['genero']
    tableTipousuario = request.POST['tipouser']
    tableActivo = request.POST['activo']

    usuario = Usuarios.objects.create(idRegistro=tableCodigo,nombre=tableNombre,identificacion=tableIdentificacion,direccion=tableDireccion,telefono=tableTelofono,usuario=tableUsuario,contrasena=tableContrasena,correo=tableCorreo,fechaNacimiento=tableNacimiento,genero=tableGenero,tipoUsuario=tableTipousuario, is_active =tableActivo)
    return redirect('../personal/')
    
def eliminarUsuario(request,idRegistro):
    usuarioEliminado = Usuarios.objects.get(IdRegistro=idRegistro)
    usuarioEliminado.delete()

    return redirect ('../personal/')


#Views de Productos by Callese la puta jeta
def registrarProducto(request):
    tableCodigo = request.POST['codigo']
    tableProducto = request.POST['producto']
    tableStock = request.POST['stock']
    tablePrecioUnitario = request.POST['precio']
    tableActivo = request.POST['activo']

    producto = Producto.objects.create(Codigo=tableCodigo,Producto=tableProducto,Stock=tableStock,Precio=tablePrecioUnitario,Activo=tableActivo)
    return redirect('../producto/')

#Views de Proveedores

def registrarProveedor(request):
    tableCodigo = request.POST['codigo']
    tableProveedor = request.POST['proveedor']
    tableCorreo= request.POST['correo']
    tableDireccion = request.POST['direccion']
    tableTelefono = request.POST['telefono']
    tableActivo = request.POST['activo']

    proveedor = Proveedore.objects.create(Codigo=tableCodigo,Proveedor=tableProveedor,Correo=tableCorreo,Direccion=tableDireccion,Telefono=tableTelefono,Activo=bool(tableActivo))
    return redirect('../proveedores/')


#Vista por Davidisito /// ESTA PUTA MIERDA QUE ES
