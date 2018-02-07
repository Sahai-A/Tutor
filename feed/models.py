from django.db import models

class User(models.Model):
	name = models.CharField(max_length=20)
	email = models.CharField(max_length=40, default = "some string")
	def __str__(self):
		return self.name
# Create your models here.
