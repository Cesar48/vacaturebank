from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CompanyUser(AbstractUser):
	companyname = models.CharField(max_length=254, verbose_name='Naam van uw bedrijf', blank=False, null=False)
	corp_email = models.EmailField(max_length=254, verbose_name='Bedrijfsemail', help_text='Op dit emailadres ontvangt u updates over uw vacatures etc', blank=False, null=False)
	desc = models.TextField(verbose_name='Omschrijving van uw bedrijf', blank=False, null=False)

	groups = None
	user_permissions = None

	def __str__(self):
		return self.companyname

class OfferType(models.Model):
	# helpt om JobOffer te filteren. Voorbeelden zijn Tech, Horeca, Administratie...
	name = models.CharField(max_length=254, verbose_name="Naam van vacaturetype", blank=False, null=False)

class JobOffer(models.Model):
	company = models.ForeignKey(CompanyUser, on_delete=models.CASCADE) #verwijder alle offers van een verwijderd bedrijf
	name = models.CharField(max_length=254, verbose_name='Vacaturenaam', blank=False, null=False)
	desc = models.TextField(verbose_name='Wat houdt de vacature in?', blank=False, null=False)

class RequiredSkill(models.Model):
	from applicants.models import JobSkill, EXP_CHOICES
	offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
	skill = models.ForeignKey(JobSkill, on_delete=models.CASCADE)
	experience = models.CharField(max_length=1, choices=EXP_CHOICES, verbose_name="Benodigde ervaring", blank=False, null=False)
