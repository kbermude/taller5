from django.db import models
from mongoengine import Document,EmbeddedDocument, fields


# Create your models here.

class Book(Document):
	title = fields.StringField()
	authors = fields.StringField()
	isbn = fields.StringField()
	rate = fields.StringField()

class User(models.Model):
	nombre=models.CharField(max_length=60)
	apellido=models.CharField(max_length=100)
	cedula=models.CharField(max_length=1)
	correo=models.CharField(max_length=50)
	fecha_nacimiento=models.DateField(_("Date"), default=datetime.date.today)
	


