# Generated by Django 2.2.5 on 2019-10-26 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('units', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField(blank=True)),
                ('contact_info', models.CharField(blank=True, max_length=255)),
                ('office_hours', models.CharField(blank=True, max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collegeWebPortal.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('capacity', models.PositiveSmallIntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_id', to='collegeWebPortal.Building')),
            ],
            options={
                'unique_together': {('number', 'building')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3)),
                ('major_1', models.CharField(max_length=255)),
                ('major_2', models.CharField(blank=True, max_length=255)),
                ('minor', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed'), ('W', 'Waitlisted')], default='O', max_length=1)),
                ('semester', models.CharField(choices=[('SP', 'Spring'), ('SU', 'Summer'), ('FA', 'Fall'), ('WI', 'Winter')], max_length=2)),
                ('schedule', models.CharField(choices=[('TBD', 'To Be Decided'), ('ONL', 'Online'), ('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('MW', 'Monday/Wednesday'), ('MWF', 'Monday/Wednesday/Friday'), ('TT', 'Tuesday/Thursday'), ('TTF', 'Tuesday/Thursday/Friday'), ('MTWTF', 'Monday-Friday')], default='TBD', max_length=5)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeWebPortal.Course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collegeWebPortal.Professor')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collegeWebPortal.Room')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeWebPortal.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(to='collegeWebPortal.Course'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.PositiveSmallIntegerField(blank=True)),
                ('grade', models.CharField(blank=True, max_length=2)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='collegeWebPortal.Section')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='collegeWebPortal.Student')),
            ],
            options={
                'unique_together': {('student', 'section')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('number', 'department')},
        ),
    ]
