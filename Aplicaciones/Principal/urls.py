from django.urls import path, include
from rest_framework import routers
from . import views

#API BY jeanlol
router = routers.DefaultRouter()
router.register(r'_usuarios',views.UsuariosViewSet)
router.register(r'_productos',views.ProductoViewSet)
router.register(r'_proveedores',views.ProveedoresViewSet)


app_name='Principal'
urlpatterns = [
    path('api', include(router.urls)),
] 

