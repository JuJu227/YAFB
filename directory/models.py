from django.db import models
from django.contrib.auth.models import Group, User

class Type(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)

	def __str__(self):
        return self.name

class GroupProfile(models.Model):
	type = models.ForrignKey(Type)
	group = models.OneToOneField(Group)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)

	def __str__(self):
        return self.name

class Employee(models.Model):
	user = models.OneToOneField(User)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	start_date = models.DateField()
	picture = models.ImageField(upload_to=None)

	def __str__(self):
        return self.name