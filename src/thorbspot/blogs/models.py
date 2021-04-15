from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=120)
	blog = models.CharField(max_length=350)
	smm = models.BooleanField()