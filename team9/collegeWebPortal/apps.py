from django.apps import AppConfig
from django.db.models.signals import post_save


class CollegewebportalConfig(AppConfig):
    name = 'collegeWebPortal'

    def ready(self):
        from django.contrib.auth.models import User
        from .signals import ensure_profile_exists

        post_save.connect(ensure_profile_exists, sender=User, dispatch_uid='ensure_profile_exists')
