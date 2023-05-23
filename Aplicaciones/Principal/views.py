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
