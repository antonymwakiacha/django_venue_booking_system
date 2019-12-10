from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Classrep
from .forms import NewClassrep

def home(request):
	return render(request,'home.html')

def new_classrep(request,):
	if request.method == 'POST':
		form = NewClassrep(request.POST)
		if form.is_valid():
			Classrep=form.save()
			return HttpResponse('registration succesful')


	else:
		form=NewClassrep()

	return render(request,'reg.html',{'form':form})

# def reg(request):
# 	return HttpResponse("Registration Succesfull")


# Create your views here.
