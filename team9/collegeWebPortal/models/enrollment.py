from django.db import models
from .section import Section
from .student import Student


class Enrollment(models.Model):
    STATUS_ENROLLED = 'ER'
    STATUS_DROPPED = 'DR'
    STATUS_INCART = 'IC'
    STATUS_SAVED = 'SA'

    STATUS_CHOICES = [
        (STATUS_ENROLLED, 'Enrolled'),
        (STATUS_DROPPED, 'Dropped'),
        (STATUS_INCART, 'In Cart'),
        (STATUS_SAVED, 'Saved'),
    ]

    student = models.ForeignKey(to=Student, on_delete=models.DO_NOTHING)
    section = models.ForeignKey(to=Section, on_delete=models.DO_NOTHING)
    credits = models.PositiveSmallIntegerField(blank=True)
    grade = models.CharField(max_length=2, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_ENROLLED)

    class Meta:
        unique_together = (('student', 'section'))
