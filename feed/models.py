from django.db import models

class User(models.Model):
	name = models.CharField(max_length=20)
	email = models.CharField(max_length=40, default = "some email address")
	phone_number = models.CharField(max_length=11, default = "123.456.7890")
	grade = models.CharField(max_length=2, default = "")
	def __str__(self):
		return self.name
		
class Tag(models.Model):
	name = models.CharField(max_length=30)
	needs_help = models.BooleanField(default = 0)
	can_help = models.BooleanField(default = 0)
	users = models.ManyToManyField(User)
