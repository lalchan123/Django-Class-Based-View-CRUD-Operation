from django.db import models


# Create your models here.
from django.urls import reverse_lazy


class Person(models.Model):
	name = models.CharField(max_length=130)
	email = models.EmailField(blank=True)
	job_title = models.CharField(max_length=30, blank=True)
	bio = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Kişi'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse_lazy('crispy:list')
