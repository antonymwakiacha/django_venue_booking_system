# Generated by Django 2.2.7 on 2020-01-21 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_classrep_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='timetable_id',
        ),
    ]
