from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'admins/index.html', {})

def general_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		login(request, user)
		if user:
			if 'next' in request.GET:
				return redirect(request.GET['next'])
			elif hasattr(user, 'companyuser'):
				return redirect('/companies/')
			else:
				return redirect('/applicants/')
	return render(request, 'login.html', {})
