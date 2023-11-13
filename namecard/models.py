from django.db import models


class Namecard(models.Model):
	Company = models.CharField(max_length=100)
	Name = models.CharField(max_length=50)
	Role = models.CharField(max_length=50)
	PhoneNumber = models.CharField(max_length=50)
	Address = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(blank=True, null=True, upload_to='images')