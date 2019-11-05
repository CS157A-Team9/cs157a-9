from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from collegeWebPortal.decorators import group_required
from collegeWebPortal.models import Course


@login_required
@group_required(settings.GROUP_STUDENTS)
def index(request):
	return render(request, 'collegeWebPortal/student/index.html')

@login_required
@group_required(settings.GROUP_STUDENTS)
def courses(request):
	return render(request, 'collegeWebPortal/student/courses.html')

@login_required
@group_required(settings.GROUP_STUDENTS)
def professors(request):
	return render(request, 'collegeWebPortal/student/professors.html')

@login_required
@group_required(settings.GROUP_STUDENTS)
def registration(request):
	page = request.GET.get('page', 1)
	course_list = Course.objects.all()
	paginator = Paginator(course_list, 15)

	try:
		courses = paginator.page(page)
	except PageNotAnInteger:
		courses = paginator.page(1)
	except EmptyPage:
		courses = paginator.page(1)

	return render(request, 'collegeWebPortal/student/registration.html', {'courses' : courses})
