from django.db import models
from django.contrib.auth.models import Group, User

class Type(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)

class GroupProfile(models.Model):
	type = models.ForeignKey(Type)
	group = models.OneToOneField(Group)
	description = models.CharField(max_length=300)

class Employee(models.Model):
	user = models.OneToOneField(User)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	start_date = models.DateField()

class Message(models.Model):
	writer = models.OneToOneField(User)
	text = models.CharField(max_length=300)
	time_stamp = models.DateField(auto_now=True)
