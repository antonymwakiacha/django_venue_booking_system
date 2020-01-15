from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignUpForm


def home(request):
	return render(request,'home.html')

def signup(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			return redirect('success')

	else:
		form=SignUpForm()
	return render(request,'reg.html',{'form':form})

def success(request):
	return render(request,'reg_successful.html')
# Create your views here.
