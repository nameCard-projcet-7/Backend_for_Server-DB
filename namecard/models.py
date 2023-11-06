from django.db import models


class Namecard(models.Model):
	company = models.CharField(max_length=200)
	name = models.TextField()
	role = models.TextField()
	phonenumber = models.TextField()
	address = models.TextField()
	email = models.TextField()
	