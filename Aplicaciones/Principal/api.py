from .models import Usuarios,Producto,Proveedore
from rest_framework import viewsets, permissions
from .serializer import UsuariosSerializer,ProductoSerializer,ProveedoreSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuariosSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedore.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedoreSerializer