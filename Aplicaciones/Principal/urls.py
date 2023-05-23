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
    path('', views.base , name='base'),
    path('inicio/', views.inicio, name='inicio'),
    path('personal/', views.personal, name='personal'),
    path('producto/', views.productos, name='productos'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('facturas/', views.facturas, name='facturas'),
    path('verUsuarios/',views.verUsuarios, name='verUsuarios'),
    path('login/', views.login, name='login'),
    path('verProductos/',views.verProductos, name='verProductos'),
    path('verProveedores/',views.verProveedores, name='verProveedores'),
    #Paths para personal
    path('registrarUsuario/', views.registrarUsuario),
    path('eliminarUsuario/<idRegistro>', views.eliminarUsuario),
    #Paths para producto
    path('registrarProducto/', views.registrarProducto),
    #Paths para Proveedores
    path('registrarProveedor/',views.registrarProveedor),
    #api by jeanlol
    path('api', include(router.urls)),
] 

