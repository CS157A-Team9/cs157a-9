from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def index(request):
    groups = request.user.groups

    if (groups.filter(name__exact=settings.GROUP_PROFESSORS).exists()):
        return HttpResponseRedirect(reverse('professor'))

    return HttpResponseRedirect(reverse('student'))
