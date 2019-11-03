from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('Home', views.index, name='index'),
    path('MyProfessors', views.myProfessor, name='myProfessor'),
    path('Registration', views.registration, name='registration'),
    path('MyCourses', views.myCourses, name='myCourses')
]
