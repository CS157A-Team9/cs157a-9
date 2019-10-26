from django.db import models


class Building(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=255)
