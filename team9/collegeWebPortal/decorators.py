from django.contrib.auth.decorators import user_passes_test


def group_required(*group_names):
    """Requires user to be a member of at least one of the specified groups"""

    def in_groups(user):
        if user and user.is_authenticated:
            return bool(user.groups.filter(name__in=group_names))
        return False

    return user_passes_test(in_groups)
