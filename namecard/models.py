from django.db import models


class Namecard(models.Model):
	Company = models.CharField(max_length=100)
	Name = models.CharField(max_length=50)
	Role = models.CharField(max_length=50)
	PhoneNumber = models.CharField(max_length=50)
	Address = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)

class PostImage(models.Model):
	img = models.ImageField(upload_to='media/images/')
	#file_dated = models.DateField(auto_now=True)
	# image = models.ImageField(blank=True, null=True,upload_to='media/images')
