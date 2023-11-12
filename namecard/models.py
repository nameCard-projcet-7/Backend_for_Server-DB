from django.db import models


class Namecard(models.Model):
	Company = models.CharField(max_length=100)
	Name = models.CharField(max_length=50)
	Role = models.CharField(max_length=50)
	PhoneNumber = models.CharField(max_length=50)
	Address = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)
	