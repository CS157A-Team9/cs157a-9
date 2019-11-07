from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from collegeWebPortal.decorators import group_required
from collegeWebPortal.models import Course, Department, Section


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
	dept = request.GET.get('dept', None)

	if (dept is not None and Department.objects.filter(pk=dept.upper()).exists()):
		course_list = Course.objects.filter(department__code__iexact=dept)
	else:
		course_list = Course.objects.all()

	paginator = Paginator(course_list.order_by('number'), 15)

	try:
		courses = paginator.page(page)
	except PageNotAnInteger:
		courses = paginator.page(1)
	except EmptyPage:
		courses = paginator.page(1)

	context = {'courses': courses, 'department': dept}

	return render(request, 'collegeWebPortal/student/registration.html', context)

@login_required
@group_required(settings.GROUP_STUDENTS)
def sectionList(request, course_id):
	page = request.GET.get('page', 1)
	course = get_object_or_404(Course, pk=course_id)
	section_list = Section.objects.filter(course=course).order_by('number')
	paginator = Paginator(section_list, 15)

	try:
		sections = paginator.page(page)
	except PageNotAnInteger:
		sections = paginator.page(1)
	except EmptyPage:
		sections = paginator.page(1)

	context = {'course': course, 'sections': sections}

	return render(request, 'collegeWebPortal/student/section-list.html', context)
