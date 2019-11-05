from django.db import models
from django.contrib.auth.models import User


"""
I have chosen explicitly to use a one-to-one field to the
default User model instead of using multi-table inheritance
due to some known issues with the latter
"""
class ProfileBase(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.user
