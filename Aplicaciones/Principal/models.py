import random
import string
from django.db import models

#API by jeanlol





#La siguiente funcion genera un numero aleatorio de 6 digitos
def numeroRandom():

    return ''.join(random.choices(string.digits, k=6))


# Create your models here.
class Usuarios(models.Model):
    idRegistro = models.CharField(max_length=6, primary_key=True, default=numeroRandom)
    nombre = models.CharField(max_length=30)
    identificacion = models.PositiveIntegerField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=25)
    correo = models.EmailField()
    fechaNacimiento = models.DateField()
    
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    )
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    
    TIPO_USUARIO_CHOICES = (
        ('A', 'Administrador'),
        ('V', 'Vendedor')
    )
    tipoUsuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        texto ="Nombre: {0} , Usuario: {1}"
        return texto.format(self.nombre, self.usuario)

    def save(self, *args, **kwargs):
        if not self.idRegistro:
            self.idRegistro = numeroRandom()
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'usuarios_'


#DATABASE DE PRODUCTOS
class Producto(models.Model):
    Codigo = models.PositiveIntegerField(primary_key=True, default=numeroRandom)
    Producto = models.CharField(max_length=120)
    Stock = models.PositiveIntegerField()
    Precio = models.CharField(max_length=20)
    Activo = models.BooleanField(default=True)


    def __str__(self):
        texto ="Codigo: {0} , Producto: {1}"
        return texto.format(self.Codigo, self.Producto)


    def save(self, *args, **kwargs):
        if not self.Codigo:
            self.Codigo = numeroRandom()
        super().save(*args, **kwargs)
    


#DATABASE DE PROVEEDORES
class Proveedore(models.Model):
    Codigo = models.PositiveIntegerField(primary_key=True, default=numeroRandom)
    Proveedor = models.CharField(max_length=120)
    Correo = models.CharField(max_length=120)
    Direccion = models.CharField(max_length=120)
    Telefono = models.PositiveIntegerField()
    Activo = models.BooleanField(default=True)

    def __str__(self):
        texto ="Codigo: {0} , Proveedor: {1}"
        return texto.format(self.Codigo, self.Proveedor)

    def save(self, *args, **kwargs):
        if not self.Codigo:
            self.Codigo = numeroRandom()
        super().save(*args, **kwargs)
    







