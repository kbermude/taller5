from django.db import models
from mongoengine import Document,EmbeddedDocument, fields
import datetime

# Create your models here.

class Book(Document):
	title = fields.StringField()
	authors = fields.StringField()
	isbn = fields.StringField()
	rate = fields.StringField()

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    contrasena = models.CharField(max_length=10)
    nombreUsuario = models.CharField(max_length=10)

class Persona(models.Model):
    cedula = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE())
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    cumpleanios= models.DateField()
