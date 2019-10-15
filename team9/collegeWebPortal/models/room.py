from django.db import models
from .building import Building
class Room(models.Model):
	id = models.AutoField(primary_key=True)
	number = models.IntegerField("")
	capacity = models.IntegerField()
	building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='building_id')

	class Meta:
		unique_together= (('number', 'building'))