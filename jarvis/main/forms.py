from django import forms
from .models import Classrep

class NewClassrep(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Classrep
		fields=['full_name','reg_no','telephone_number','email','cohort','password']