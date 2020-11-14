from django.contrib.auth.models import User
from django.db import models

# Create your models here.

EXP_CHOICES = (
	(0, "Onervaren"),
	(1, "Beginner"),
	(2, "Gemiddeld"),
	(3, "Ervaren"),
	(4, "Goed"),
	(5, "Expert"),
)

class ApplicantProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) #TODO: replace User with SSO-user
	desc = models.TextField(verbose_name="Omschrijving", blank=False, null=False)

class SkillType(models.Model):
	# helpt om JobSkill te filteren. Voorbeelden zijn Tech, Soft skils, Design...
	name = models.CharField(max_length=254, verbose_name="Naam van vaardigheidstype", blank=False, null=False)

class JobSkill(models.Model):
	name = models.CharField(max_length=254, verbose_name="Naam van de vaardigheid", blank=False, null=False)
	desc = models.TextField(verbose_name="Omschrijving van de vaardigheid", blank=False, null=False)
	type_of_skill = models.ForeignKey(SkillType, on_delete=models.SET_NULL, verbose_name="Type vaardigheid", blank=True, null=True) #verwijderde categorieën of losse skills zijn mogelijk

class AcquiredSkill(models.Model):
	applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
	skill = models.ForeignKey(JobSkill, on_delete=models.CASCADE)
	experience = models.CharField(max_length=1, choices=EXP_CHOICES, verbose_name="Ervaring", blank=False, null=False)
