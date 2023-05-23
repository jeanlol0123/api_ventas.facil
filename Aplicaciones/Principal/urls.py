from django.urls import path, include
from rest_framework import routers
from .api import UsuariosViewSet,ProductoViewSet,ProveedoresViewSet

#API BY jeanlol
router = routers.DefaultRouter()

rut= 'Aplicaciones\Principal'

router.register('api/usuarios', UsuariosViewSet, rut)
router.register('api/proveedores', ProveedoresViewSet, rut)
router.register('api/productos', ProductoViewSet, rut)

urlpatterns = [
    path('api', include(router.urls))
]

