from django.urls import path, include
from rest_framework import routers
from .api import UsuariosViewSet,ProductoViewSet,ProveedoresViewSet

#API BY jeanlol
router = routers.DefaultRouter()


router.register('api/usuarios', UsuariosViewSet, 'usuarios')
router.register('api/proveedores', ProveedoresViewSet, 'proveedores')
router.register('api/productos', ProductoViewSet, 'productos')

urlpatterns = router.urls

