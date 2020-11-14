from django import forms
from django.contrib.auth.forms import UserCreationForm

from companies.models import *


class SignUpForm_Companies(UserCreationForm):

	class Meta:
		model = CompanyUser
		fields = ('username', 'companyname', 'desc', 'corp_email', 'password1', 'password2',)

class CreateJobOfferForm(forms.ModelForm):

	class Meta:
		model = JobOffer
		exclude = ('company',)
