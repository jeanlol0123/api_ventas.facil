from django.urls import path, include
from rest_framework import routers
from .api import UsuariosViewSet,ProductoViewSet,ProveedoresViewSet

#API BY jeanlol
router = routers.DefaultRouter()


router.register('api/usua', UsuariosViewSet, 'usuarios')
router.register('api/prove', ProveedoresViewSet, 'proveedores')
router.register('api/produ', ProductoViewSet, 'productos')

urlpatterns = router.urls

