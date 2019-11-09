from django.urls import path

from .views import common, professor, student

urlpatterns = [
	path('', common.index, name='index'),
    path('professor', professor.index, name='professor'),
    path('professor/courses', professor.courses, name='professor-courses'),
    path('professor/profile', professor.profile, name='professor-profile'),
    path('professor/edit_bio', professor.edit_bio, name='professor-profile-edit-bio'),
    path('professor/edit_contact', professor.edit_contact, name='professor-profile-edit-contact'),
    path('professor/edit_hour', professor.edit_hour, name='professor-profile-edit-hour'),
    path('student', student.index, name='student'),
    path('student/courses', student.courses, name='student-courses'),
    path('student/professors', student.professors, name='student-professors'),
    path('student/registration', student.registration, name='student-registration'),
    path('student/registration/<int:course_id>', student.sectionList, name='student-registration-course'),
    path('student/registration/section/<int:section_id>', student.sectionRegister, name='student-section-register'),
]
