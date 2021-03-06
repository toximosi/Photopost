""" USER model """
"""NOTE:bibliografia:
    https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
    https://docs.djangoproject.com/en/4.0/ref/models/fields/
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/
    """
#importaciones ---------------------------------------------------------
#django
from django.db import models
from django.contrib.auth.models import User #heredamos de user de django

# Code ---------------------------------------------------------
#Nos vasamos en el modelo de usuario de Django admin
class Profile(models.Model):#en vez de USER le llamamos Profile por perfil de usuario
    """Profile model 
    modelo Proxy que extiende la base de datos con otra información"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="nombre usuario")
    #? on_delete: que hace si se borra el user->en este caso acturá como un SQL
    first_name = models.CharField(max_length=50, verbose_name="Nombre"),
    last_name = models.CharField(max_length=50, verbose_name="Apellidos"),
    biography = models.TextField(blank=True, verbose_name="Biografía") 
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    #? blank=True, que permite que se quede vacio
    website = models.URLField(max_length=200, blank=True, verbose_name="Web")
    picture = models.ImageField(upload_to='users/pictures',blank=True,null=True, verbose_name="avatar" )#!Necesario instalar pip install Pillow
    #upload_to: donde se guardarán las imágenes
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creación")#fechas de creación 
    modified = models.DateTimeField(auto_now=True, verbose_name="Modificación")#fecha de modificación 
    
    def __str__(self): #representacion en string en admin
        return f"user: {self.user} - first_name: {self.first_name} - last_name: {self.last_name} - biography: {self.biography} - website: {self.website} - picture: {self.picture} - created: {self.created} - modified: {self.modified}" 

        