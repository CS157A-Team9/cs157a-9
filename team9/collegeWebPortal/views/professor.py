from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from collegeWebPortal.decorators import group_required


@login_required
@group_required(settings.GROUP_PROFESSORS)
def index(request):
    pass

@login_required
@group_required(settings.GROUP_PROFESSORS)
def courses(request):
    pass

@login_required
@group_required(settings.GROUP_PROFESSORS)
def profile(request):
    pass
