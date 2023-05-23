from django.urls import path, include
from rest_framework import routers
from .api import UsuariosViewSet,ProductoViewSet,ProveedoresViewSet

#API BY jeanlol
router = routers.DefaultRouter()
router.register(r'api_usuarios',UsuariosViewSet)
router.register(r'api_productos',ProductoViewSet)
router.register(r'api_proveedores',ProveedoresViewSet)

urlpatterns = router.urls

