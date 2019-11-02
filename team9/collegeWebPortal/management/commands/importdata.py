from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import loaddata

# Note: Fixture order is important to prevent Django relational errors
fixtures = [
    'groups', 'users', 'buildings', 'departments', 'courses', 'professors', 'rooms', 'sections'
]

class Command(BaseCommand):
    help = 'Imports app fixture data into the database'

    def handle(self, *args, **options):
        for fixture in fixtures:
            management.call_command(loaddata.Command(), fixture)
