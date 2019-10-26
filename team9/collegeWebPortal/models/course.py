from django.db import models
from .department import Department


class Course(models.Model):
	number = models.PositiveSmallIntegerField()
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=1000)
	department = models.ForeignKey(to=Department, on_delete=models.CASCADE)
	prerequisites = models.ManyToManyField(to='Course')
	units = models.PositiveSmallIntegerField()

	class Meta:
		unique_together = (('number', 'department'))