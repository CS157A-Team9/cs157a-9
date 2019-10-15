from django.db import models
from .department import Department


class Course(models.Model):
	#id = models.AutoField(primary_key=True)
	number = models.IntegerField()
	name = models.CharField(max_length=255, primary_key=True)
	description = models.CharField(max_length=255)
	department = models.ForeignKey(to=Department, on_delete=models.CASCADE)

	class Meta:
		unique_together= (('number', 'department'))