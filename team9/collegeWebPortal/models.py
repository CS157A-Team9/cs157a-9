from django.db import models

# Create your models here.
class Student(models.Model):
	student_id = models.IntegerField(max_length=9)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def getFUllName(self):
		return '%s %s' % (self.first_name, self.last_name)
		