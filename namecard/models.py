from django.db import models


class Namecard(models.Model):
	Company = models.CharField(max_length=100)
	Name = models.CharField(max_length=50)
	Role = models.CharField(max_length=50)
	PhoneNumber = models.CharField(max_length=50)
	Address = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)

class PostImage(models.Model):
	title = models.TextField(max_length=200,null=True)
	contents = models.CharField(max_length=50,null=True)
	img = models.ImageField(upload_to='images/',null=True, blank=True)
	uploaded_at = models.DateTimeField(auto_now=True)
	
