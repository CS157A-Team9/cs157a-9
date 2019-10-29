from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
	return render(request, 'collegeWebPortal/index.html')

def myProfessor(request):
	return render(request, 'collegeWebPortal/MyProfessors.html')

def myCourses(request):
	return render(request, 'collegeWebPortal/MyCourses.html')

def registration(request):
	return render(request, 'collegeWebPortal/Registration.html')