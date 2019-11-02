from django.db import models
from .section import Section
from .student import Student


class Enrollment(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.DO_NOTHING)
    section = models.ForeignKey(to=Section, on_delete=models.DO_NOTHING)
    credits = models.PositiveSmallIntegerField(blank=True)
    grade = models.CharField(max_length=2, blank=True)

    class Meta:
        unique_together = (('student', 'section'))
