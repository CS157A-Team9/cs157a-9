from django.apps import AppConfig


class CollegewebportalConfig(AppConfig):
    name = 'collegeWebPortal'

    def ready(self):
        from .signals import ensure_profile_exists
