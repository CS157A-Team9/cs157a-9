from django.contrib import admin
from .models import Building, Course, Department, Enrollment, Professor, Room, Section, Student

admin.site.register(Building)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Enrollment)
admin.site.register(Professor)
admin.site.register(Room)
admin.site.register(Section)
admin.site.register(Student)
