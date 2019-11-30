# #Constants in this class
# BOOKED='BKD'
# FREE='FR'
# STATUS_IN_T.TABLE_CHOICES=(
# 	(BOOKED,'booked'),
# 	(FREE,'free'),
# 		)
from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Classrep(models.Model):
	full_name=models.CharField(max_length=200,null=True)
	reg_no=models.CharField(max_length=200,null=True)
	telephone_number=models.CharField(max_length=200,null=True)
	email=models.CharField(max_length=200,null=True)
	cohort=models.CharField(max_length=200,null=True)
	password=models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.reg_no

class Course(models.Model):
	cohort=models.CharField(max_length=200,null=True)
	course_code=models.CharField(max_length=200,null=True)
	course_title=models.CharField(max_length=200,null=True)
	lecturers=models.CharField(max_length=200,null=True)
	department=models.CharField(max_length=200,null=True)
	contact=models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.course_code

class Cohort(models.Model):
	cohort=models.CharField(max_length=200,null=True)
	reg_no=models.CharField(max_length=200,null=True)
	no_of_students=models.CharField(max_length=200,null=True)
	courses_enrolled=models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.cohort



class ContactUs(models.Model):
	contactus_id=models.IntegerField(null=True)
	time=models.TimeField(auto_now=False)
	date=models.DateField(auto_now=False)
	reg_no=models.CharField(max_length=200,null=True)
	phone_no=models.CharField(max_length=200,null=True)
	email=models.EmailField(max_length=200,null=True)
	message=models.CharField(max_length=200,null=True)
	response=models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.contactus_id

class Venue(models.Model):
	venue_id=models.IntegerField(null=True)
	school=models.CharField(max_length=200,null=True)
	capacity=models.IntegerField(null=True)

	def __str__(self):
		return self.venue_id

class Timetable(models.Model):
	

	timetable_id=models.IntegerField(null=True)
	status=models.CharField(max_length=200,null=True)	

	venue_id=models.CharField(max_length=200,null=True)
	school=models.CharField(max_length=200,null=True)
	day_of_week=models.CharField(max_length=200,null=True)
	duration=models.CharField(max_length=200,null=True)
	cohort=models.CharField(max_length=200,null=True)
	course_code=models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.timetable_id

class Transaction(models.Model):
	#Constants in this class
	venue_id=models.IntegerField(null=True)
	time=models.TimeField(auto_now=False)
	date=models.DateField(auto_now=False)
	transaction_type=models.CharField(max_length=200,null=True)
	reg_no=models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.id



# Create your models here.
