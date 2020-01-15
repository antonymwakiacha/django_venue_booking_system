from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	fullname=forms.CharField(max_length=254,required=True)
	reg_no=forms.CharField(max_length=254,required=True)
	telephone_no=forms.CharField(max_length=254,required=True)
	email=forms.CharField(max_length=254,required=True,widget=forms.EmailInput())
	cohort=forms.CharField(max_length=254,required=True)

	class Meta:
		model=User
		fields=[
		'fullname',
		'reg_no',
		'telephone_no',
		'email',
		'cohort',
		'password1',
		'password2',
		]