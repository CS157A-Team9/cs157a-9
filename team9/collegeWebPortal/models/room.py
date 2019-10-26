from django.db import models
from .building import Building


class Room(models.Model):
	number = models.PositiveSmallIntegerField()
	capacity = models.PositiveSmallIntegerField()
	building = models.ForeignKey(to=Building, on_delete=models.CASCADE, related_name='building_id')

	class Meta:
		unique_together = (('number', 'building'))
