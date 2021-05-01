from django.db import models
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=120)
	blog = models.CharField(max_length=350)
	smm = models.BooleanField()

	def get_absolute_url(self):
		return reverse("blogs:blog", kwargs={"pk": self.id})
