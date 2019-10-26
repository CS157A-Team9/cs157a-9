from django.db import models
from .course import Course
from .professor import Professor
from .room import Room


class Section(models.Model):
	SEMESTER_SPRING = 'SP'
	SEMESTER_SUMMER = 'SU'
	SEMESTER_FALL = 'FA'
	SEMESTER_WINTER = 'WI'

	SEMESTER_CHOICES = [
		(SEMESTER_SPRING, 'Spring'),
		(SEMESTER_SUMMER, 'Summer'),
		(SEMESTER_FALL, 'Fall'),
		(SEMESTER_WINTER, 'Winter'),
	]

	STATUS_OPEN = 'O'
	STATUS_CLOSED = 'C'
	STATUS_WAITLISTED = 'W'

	STATUS_CHOICES = [
		(STATUS_OPEN, 'Open'),
		(STATUS_CLOSED, 'Closed'),
		(STATUS_WAITLISTED, 'Waitlisted'),
	]

	SCHEDULE_CHOICES = [
		('TBD', 'To Be Decided'),
		('ONL', 'Online'),
		('MON', 'Monday'),
		('TUE', 'Tuesday'),
		('WED', 'Wednesday'),
		('THU', 'Thursday'),
		('FRI', 'Friday'),
		('SAT', 'Saturday'),
		('MW', 'Monday/Wednesday'),
		('MWF', 'Monday/Wednesday/Friday'),
		('TT', 'Tuesday/Thursday'),
		('TTF', 'Tuesday/Thursday/Friday'),
		('MTWTF', 'Monday-Friday'),
	]

	course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
	number = models.PositiveIntegerField()
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_OPEN)
	semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)
	schedule = models.CharField(max_length=5, choices=SCHEDULE_CHOICES, default='TBD')
	start_date = models.DateField()
	end_date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	instructor = models.ForeignKey(to=Professor, on_delete=models.PROTECT)
	location = models.ForeignKey(to=Room, on_delete=models.PROTECT)
