from django.db import models
from .department import Department
from .course import Course

class Section(Course):
	num = models.IntegerField()
	status = models.BooleanField()
	semester = models.CharField(max_length=255)
	time = models.CharField(max_length=50)