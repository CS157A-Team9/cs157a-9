from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Professor, Student


@receiver(m2m_changed, sender=User.groups.through)
def ensure_profile_exists(sender, **kwargs):
    action = kwargs.get('action', None)

    if action == 'post_add':
        user = kwargs.get('instance')
        groups = user.groups

        if (groups.filter(name__exact='Students').exists()):
            Student.objects.get_or_create(user=user, gpa=0.00, major_1='NOT SET')

        if (groups.filter(name__exact='Professors').exists()):
            Professor.objects.get_or_create(user=user)
