from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	choices=(
		("ADMIN",'admin'),
		("USER",'member'),
		("GUIDE",'guide'),
	)
	category=models.CharField(choices=choices,default="ADMIN",max_length=100)
	picture = models.ImageField(default="default.jpg")


	def __str__(self):
		return str(self.user)

class Group(models.Model):
	group_name = models.CharField(max_length=15,null=True)
	description = models.CharField(max_length=250,null=True)
	no_of_members = models.IntegerField(null=True)
	no_of_guides = models.IntegerField(null=True)
	members = ArrayField(models.IntegerField(null=True),blank=True,default=list)
	guide = ArrayField(models.IntegerField(null=True),blank=True,default=list)
	admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.group_name

class Milestone(models.Model):
	title=models.CharField(max_length=40, null=True)
	content=models.TextField(max_length=350, null=True)
	due_date=models.DateTimeField(auto_now_add=True)
	group=models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	is_done = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Update(models.Model):
	title=models.CharField(max_length=40)
	text=models.TextField(max_length=350)
	posted_on=models.DateTimeField(auto_now_add=True)
	group=models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

class Goal(models.Model):
	title=models.CharField(max_length=140)
	milestone=models.ForeignKey(Milestone, on_delete=models.CASCADE, null=True)
	group=models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
	is_done=models.BooleanField(default=False)

	def __str__(self):
		return self.title

