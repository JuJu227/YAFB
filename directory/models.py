from django.db import models
from django.contrib.auth.models import Group, User

class Type(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)

	def __unicode__(self):
		return self.name

class GroupProfile(models.Model):
	type = models.ForeignKey(Type)
	group = models.OneToOneField(Group)
	description = models.CharField(max_length=300)

	def __unicode__(self):
		return self.group.name

class Office(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=300)

	def __unicode__(self):
		return self.name

class Employee(models.Model):
	user = models.OneToOneField(User)
	full_name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	start_date = models.DateField(auto_now=True)
	office = models.ForeignKey(Office)
	groups = models.ManyToManyField(GroupProfile)
	password = models.CharField(max_length=30)
	email = models.CharField(max_length=100, null=True)
	picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
	manager = models.ForeignKey("self", null=True, blank=True)

	def __unicode__(self):
		return self.full_name

class Message(models.Model):
	writer = models.ForeignKey(Employee)
	text = models.CharField(max_length=300)
	time_stamp = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.time_stamp)
