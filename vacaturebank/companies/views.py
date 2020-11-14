from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from django.http import HttpResponse

from companies.forms import SignUpForm_Companies

# Create your views here.

def index(request):
	return render(request, 'companies/index.html', {})

def signup(request):
	form = SignUpForm_Companies(request.POST)
	if request.method == 'POST' and form.is_valid():
		user = form.save()
		login(request, user)
		return redirect('index')
	return render(request, 'companies/signup.html', {'form': form})
