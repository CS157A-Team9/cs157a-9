from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from collegeWebPortal.forms.common import ConfirmForm
from collegeWebPortal.decorators import group_required
from collegeWebPortal.models import Course, Department, Enrollment, Section, Student, Professor


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@login_required
@group_required(settings.GROUP_STUDENTS)
def index(request):
	def get_scheduled(uid):
		with connection.cursor() as cursor:
			cursor.execute(
				"SELECT collegeWebPortal_course.name, collegeWebPortal_section.*, collegeWebPortal_building.name AS 'building', collegeWebPortal_room.number FROM collegeWebPortal_section \
				JOIN collegeWebPortal_course ON collegeWebPortal_course.id = collegeWebPortal_section.course_id \
				JOIN collegeWebPortal_room ON collegeWebPortal_room.id = collegeWebPortal_section.location_id \
				JOIN collegeWebPortal_building ON collegeWebPortal_building.code = collegeWebPortal_room.building_id \
				WHERE start_date <= CURDATE() AND end_date >= CURDATE() AND collegeWebPortal_section.id IN \
				(SELECT section_id FROM collegeWebPortal_enrollment WHERE student_id = %s AND status = %s)",
				[uid, Enrollment.STATUS_ENROLLED])
			rows = dictfetchall(cursor)
		return rows
	
	context = {
		'scheduled': get_scheduled(request.user.id)
	}

	return render(request, 'collegeWebPortal/student/index.html', context)

@login_required
@group_required(settings.GROUP_STUDENTS)
def courses(request):
	dropped = request.GET.get('dropped', 0)
	section_id = request.GET.get('section_id', 0)

	# TODO: Optimize query and filter by the current semester
	enrollment = Enrollment.objects.filter(student__user=request.user, status=Enrollment.STATUS_ENROLLED)
	sections = [x.section for x in enrollment]

	context = {
		'dropped': dropped,
		'section_id': section_id,
		'sections': sections,
	}

	return render(request, 'collegeWebPortal/student/courses.html', context)

@login_required
@group_required(settings.GROUP_STUDENTS)
def professors(request):
	enrollment = Enrollment.objects.filter(student__user=request.user, status=Enrollment.STATUS_ENROLLED)
	professor_list = [p.section.instructor for p in enrollment]
	return render(request, 'collegeWebPortal/student/professors.html', {'professor_list': professor_list})

@login_required
@group_required(settings.GROUP_STUDENTS)
def all_professors(request):
	professor_list = Professor.objects.all()
	list_professor = False
	return render(request, 'collegeWebPortal/student/all-professors.html', {'list_professor': list_professor, 'professor_list': professor_list})

@login_required
@group_required(settings.GROUP_STUDENTS)
def list_professor_info(request, first_name, last_name):
	professor = Professor.objects.filter(user__first_name=first_name, user__last_name=last_name)
	list_professor = True
	return render(request, 'collegeWebPortal/student/profile.html', {'list_professor': list_professor, 'professor': professor})


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
	section_id = request.GET.get('section_id', 0)
	cart_added = request.GET.get('cart_added', 0)
	enrolled = request.GET.get('enrolled', 0)
	saved = request.GET.get('saved', 0)

	course = get_object_or_404(Course, pk=course_id)
	section_list = Section.objects.filter(course=course).order_by('number')
	paginator = Paginator(section_list, 15)

	try:
		sections = paginator.page(page)
	except PageNotAnInteger:
		sections = paginator.page(1)
	except EmptyPage:
		sections = paginator.page(1)

	status_dict = {
		'enrolled': set(),
		'incart': set(),
		'saved': set(),
	}

	for e in Enrollment.objects.filter(section__in=sections):
		if e.status == Enrollment.STATUS_ENROLLED:
			status_dict['enrolled'].add(e.section)
		elif e.status == Enrollment.STATUS_INCART:
			status_dict['incart'].add(e.section)
		elif e.status == Enrollment.STATUS_SAVED:
			status_dict['saved'].add(e.section)

	context = {
		'course': course,
		'sections': sections,
		'status_dict': status_dict,
		'section_id': section_id,
		'cart_added': cart_added,
		'enrolled': enrolled,
		'saved': saved,
	}

	return render(request, 'collegeWebPortal/student/section-list.html', context)

@login_required
@group_required(settings.GROUP_STUDENTS)
def sectionRegister(request, section_id):
	section = get_object_or_404(Section, pk=section_id)

	if request.method == 'POST':
		form = ConfirmForm(request.POST)

		if form.is_valid():
			# Ensure student enrolls in sections only once
			if not Enrollment.objects.filter(student__user=request.user, section=section).exists():
				student = Student.objects.get(pk=request.user.id)
				Enrollment.objects.create(student=student, section=section, credits=0)

			return HttpResponseRedirect(reverse('student'))
	else:
		form = ConfirmForm()

	context = {'form': form, 'section': section}

	return render(request, 'collegeWebPortal/student/section-register.html', context)

@login_required
@group_required(settings.GROUP_STUDENTS)
def sectionDrop(request, section_id):
	section = get_object_or_404(Section, pk=section_id)

	if request.method == 'POST':
		form = ConfirmForm(request.POST)

		if form.is_valid():
			enrollment = Enrollment.objects.filter(student__user=request.user, section=section)
			enrollment.delete()
			return HttpResponseRedirect(reverse('student-courses') + ("?dropped=1&section_id=%d" % section.number))
	else:
		form = ConfirmForm()

	context = {'form': form, 'section': section}

	return render(request, 'collegeWebPortal/student/section-drop.html', context)

@login_required
@group_required(settings.GROUP_STUDENTS)
def processAction(request, section_id, action_type):
	section = get_object_or_404(Section, pk=section_id)
	enrollment = Enrollment.objects.filter(student__user=request.user, section__id__exact=section_id)

	if action_type == 1:
		param = 'enrolled'
		status = Enrollment.STATUS_ENROLLED
	elif action_type == 2:
		param = 'cart_added'
		status = Enrollment.STATUS_INCART
	elif action_type == 3:
		param = 'saved'
		status = Enrollment.STATUS_SAVED
	else:
		return HttpResponseRedirect(reverse('student-registration'))

	if enrollment:
		enrollment.update(status=status)
	else:
		student = Student.objects.get(pk=request.user.id)
		Enrollment.objects.create(student=student, section=section, credits=0, status=status)

	url = reverse('student-registration-course', kwargs={'course_id': section.course.id})
	return HttpResponseRedirect("%s?%s=1&section_id=%d" % (url, param, section.number))

@login_required
@group_required(settings.GROUP_STUDENTS)
def checkout(request):
	enrollment = Enrollment.objects.filter(student__user=request.user, status=Enrollment.STATUS_INCART)
	sections = [x.section for x in enrollment]

	context = {'sections': sections}

	if request.method == 'POST':
		status_dict = {
			'enrolled': set(),
			'removed': set(),
		}

		for e in enrollment:
			action = request.POST.get("section_%d" % e.section.id)

			if action == 'register':
				e.status = Enrollment.STATUS_ENROLLED
				e.save()
				status_dict['enrolled'].add(e.section)
			elif action == 'remove':
				e.delete()
				status_dict['removed'].add(e.section)

		context['submitted'] = True
		context['status_dict'] = status_dict

	return render(request, 'collegeWebPortal/student/checkout.html', context)

@login_required
@group_required(settings.GROUP_STUDENTS)
def savedCourses(request):
	enrollment = Enrollment.objects.filter(student__user=request.user, status=Enrollment.STATUS_SAVED)
	sections = [x.section for x in enrollment]

	context = {'sections': sections}

	if request.method == 'POST':
		status_dict = {
			'added': set(),
			'removed': set(),
		}

		for e in enrollment:
			action = request.POST.get("section_%d" % e.section.id)

			if action == 'add':
				e.status = Enrollment.STATUS_INCART
				e.save()
				status_dict['added'].add(e.section)
			elif action == 'remove':
				e.delete()
				status_dict['removed'].add(e.section)

		context['submitted'] = True
		context['status_dict'] = status_dict

	return render(request, 'collegeWebPortal/student/saved-courses.html', context)
