from rest_framework import serializers
from .models import Usuarios,Producto,Proveedore

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        fields= '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= '__all__'

class ProveedoreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proveedore
        fields= '__all__'

