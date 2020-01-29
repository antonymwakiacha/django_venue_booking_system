from django.shortcuts import render,redirect
#from django.contrib.auth.models import User
from .forms import SignUpForm,UserLoginForm
from django.contrib.auth import get_user_model,authenticate,login,logout
User=get_user_model()



def home(request):
	return render(request,'home.html')

def login_view(request):
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		reg_no=form.cleaned_data.get("reg_no")
		password=form.cleaned_data.get("password")
		user=authenticate(reg_no=reg_no,password=password)
		login(request,user)
		return redirect('loggedin')

	return render(request,"login.html",{"form":form})

def loggedin(request):
	return render(request,'loggedin.html')

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
