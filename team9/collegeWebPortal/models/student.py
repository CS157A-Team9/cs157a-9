from django.db import models
from .profile_base import ProfileBase


class Student(ProfileBase):
	gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
	major_1 = models.CharField(max_length=255)
	major_2 = models.CharField(max_length=255, blank=True)
	mminor = models.CharField(max_length=255, blank=True)
