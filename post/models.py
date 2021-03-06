""" Posts models"""
#bibliografia:
    #https://docs.djangoproject.com/en/4.0/ref/models/fields/
# importaciones ------------------------------------------------------
#Django
from django.db import models
from django.contrib.auth.models import User#heredamos de user de django
# users
from user.models import Profile

#modelos -------------------------------------------------------------
class User(models.Model):

    def __str__(self):
        return f"user: {self.user} - email: {self.email} - password: {self.password} - first_name: {self.first_name} - last_name: {self.last_name} - bio: {self.bio} - birthdate: {self.birthdate} - created: {self.created} - modified: {self.modified} - is_admin: {self.is_admin}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#on_delete, cuando se borre el usuario se borren los post
    #? unique: para que no se repita el mail en la base de datos
    #profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    #? unique: para que no se repita el mail en la base de datos
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    #?auto_now_add: que se cree automáticamente
    modified = models.DateTimeField(auto_now=True)
    #?auto_now: que se cree automáticamente

    def __str__(self):
           return '{} by @{}'.format(self.title, self.user.username)