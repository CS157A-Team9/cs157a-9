from django.urls import path

from .views import common, professor, student

urlpatterns = [
	path('', common.index, name='index'),
    path('professor', professor.index, name='professor'),
    path('professor/courses', professor.courses, name='professor-courses'),
    path('professor/profile', professor.profile, name='professor-profile'),
    path('student', student.index, name='student'),
    path('student/courses', student.courses, name='student-courses'),
    path('student/professors', student.professors, name='student-professors'),
    path('student/registration', student.registration, name='student-registration'),
]
