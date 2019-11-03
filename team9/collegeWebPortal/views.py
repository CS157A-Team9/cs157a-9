from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course


@login_required
def index(request):
	return render(request, 'collegeWebPortal/index.html')

@login_required
def myProfessor(request):
	return render(request, 'collegeWebPortal/MyProfessors.html')

@login_required
def myCourses(request):
	return render(request, 'collegeWebPortal/MyCourses.html')

@login_required
def registration(request):
	courses = Course.objects.all()
	return render(request, 'collegeWebPortal/Registration.html', {'courses' : courses})
