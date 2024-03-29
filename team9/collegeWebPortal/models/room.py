from django.db import models
from .building import Building


class Room(models.Model):
	number = models.CharField(max_length=8)
	capacity = models.PositiveSmallIntegerField()
	building = models.ForeignKey(to=Building, on_delete=models.CASCADE, related_name='building_id')

	class Meta:
		unique_together = (('number', 'building'))

	def __str__(self):
		return "%s%s" % (self.building.code, self.number)
