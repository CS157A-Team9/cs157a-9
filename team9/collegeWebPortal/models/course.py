from django.db import models
from .department import Department


class Course(models.Model):
	number = models.CharField(max_length=8)
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=1000, blank=True)
	department = models.ForeignKey(to=Department, on_delete=models.CASCADE)
	prerequisites = models.ManyToManyField(to='Course', blank=True)
	units = models.PositiveSmallIntegerField()

	class Meta:
		unique_together = (('number', 'department'))

	def __str__(self):
		return "%s" % self.name
