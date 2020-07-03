from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
TIPO_CHOICES = (
        ('Cereal', 'Cereal'),
        ('Frutas', 'Fruta'),
        ('Verduras', 'Verdura'),
        ('Lácteos', 'Lácteos'),
    )

class ComprarArticulo(models.Model): #single. 
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=5000, blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        view_name = "detail"
        return reverse(view_name, kwargs={"pk": self.id})
    
class Nota(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=5000)

