from django.contrib.auth.models import User
from .models import Professor, Student


def ensure_profile_exists(sender, **kwargs):
    if (kwargs.get('created', False)):
        user = kwargs.get('instance')
        groups = user.groups

        if (groups.filter(name__exact='Students').exists()):
            Student.objects.get_or_create(user=user, major_1='NOT SET')

        if (groups.filter(name__exact='Professors').exists()):
            Professor.objects.get_or_create(user=user)
