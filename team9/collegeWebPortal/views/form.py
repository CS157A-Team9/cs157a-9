from django import forms

class SemesterForm(forms.Form):
	CHOICES = (('FA', 'Fall 2019'),('SP', 'Spring 2020'),)
	semester = forms.ChoiceField(choices=CHOICES, label='Current semester')