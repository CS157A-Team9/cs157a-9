from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from collegeWebPortal.decorators import group_required
from collegeWebPortal.models import Professor
from collegeWebPortal.models import Section
from collegeWebPortal.models import Course

@login_required
@group_required(settings.GROUP_PROFESSORS)
def index(request):
    return render(request, 'collegeWebPortal/professor/index.html')

@login_required
@group_required(settings.GROUP_PROFESSORS)
def courses(request):
	sections = Section.objects.filter(instructor=request.user.id)
	classes = [(x, x.course) for x in sections]
	return render(request, 'collegeWebPortal/professor/courses.html', {'classes': classes})

@login_required
@group_required(settings.GROUP_PROFESSORS)
def profile(request):
	professor = Professor.objects.get(pk=request.user.id)
	return render(request, 'collegeWebPortal/professor/profile.html', {'usr': professor})

@login_required
@group_required(settings.GROUP_PROFESSORS)
def edit_bio(request):
	if request.method == 'POST':
		bio = request.POST.get('bio', None)
		try: 
			professor = Professor.objects.get(pk=request.user.id)
			professor.bio = bio
			professor.save()
			#return render(request, 'collegeWebPortal/professor/profile.html', {'usr': professor})
			return redirect('/professor/profile')
		except Professor.DoesNotExist:
			return HttpResponse("error")
	else:
		professor = Professor.objects.get(pk=request.user.id)
		showbioform = "True"
		return render(request, 'collegeWebPortal/professor/profile.html', {'usr': professor, 'showbioform': showbioform})


@login_required
@group_required(settings.GROUP_PROFESSORS)
def edit_contact(request):
	if request.method == 'POST':
		contact = request.POST.get('contact', None)
		try: 
			professor = Professor.objects.get(pk=request.user.id)
			professor.contact_info = contact
			professor.save()
			#return render(request, 'collegeWebPortal/professor/profile.html', {'usr': professor})
			return redirect('/professor/profile')
		except Professor.DoesNotExist:
			return HttpResponse("error")
	else:
		professor = Professor.objects.get(pk=request.user.id)
		showcontactform = "True"
		return render(request, 'collegeWebPortal/professor/profile.html', {'usr': professor, 'showcontactform': showcontactform})


@login_required
@group_required(settings.GROUP_PROFESSORS)
def edit_hour(request):
	if request.method == 'POST':
		hour = request.POST.get('hour', None)
		try: 
			professor = Professor.objects.get(pk=request.user.id)
			professor.office_hours = hour
			professor.save()
			#return render(request, 'collegeWebPortal/professor/profile.html', {'usr': professor})
			return redirect('/professor/profile')
		except Professor.DoesNotExist:
			return HttpResponse("error")
	else:
		professor = Professor.objects.get(pk=request.user.id)
		showhourform = "True"
		return render(request, 'collegeWebPortal/professor/profile.html', {'usr': professor, 'showhourform': showhourform})
