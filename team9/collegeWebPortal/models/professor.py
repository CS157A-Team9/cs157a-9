from django.db import models
from .department import Department
from .profile_base import ProfileBase


class Professor(ProfileBase):
    bio = models.TextField(blank=True)
    contact_info = models.CharField(max_length=255, blank=True)
    office_hours = models.CharField(max_length=255, blank=True)
    department = models.ForeignKey(to=Department, on_delete=models.PROTECT)
