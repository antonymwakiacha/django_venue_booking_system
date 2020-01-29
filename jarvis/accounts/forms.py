#from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model,authenticate,login,logout
User=get_user_model()

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


class UserLoginForm(forms.Form):
	reg_no=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		reg_no=self.cleaned_data.get("reg_no")
		password=self.cleaned_data.get("password")

		if reg_no or password:
			user=authenticate(reg_no=reg_no,password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")

			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")

			if not user.is_active:
				raise forms.ValidationError("This user is no longer active")

		return super(UserLoginForm,self).clean(*args,**kwargs)