from django.db import models
from django.utils import timezone

class Subscriber(models.Model):
	email = models.CharField(max_length=100)
	signup_date = models.DateTimeField("signup date")
	
	def __str__(self):
		return(self.email)

class Post(models.Model):
	content = models.CharField(max_length=1500)
	posted_date = models.DateTimeField("posted date")
	upvotes = models.IntegerField(default=0)
	
	def __str__(self):
		return("Post from " + str(self.posted_date))

class Image(models.Model):
	image_file_name = models.CharField(max_length=99)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return(self.image_file_name)
