from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from applicants.models import JobSkill, SkillType
from companies.forms import *
from companies.models import *

# Create your views here.

def signup(request):
	form = SignUpForm_Companies(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		user = form.save()
		login(request, user)
		return redirect('index')
	return render(request, 'companies/signup.html', {'form': form})

def index(request):
	if not request.user.is_authenticated:
		return HttpResponse('Unauthorized', status=401)
	return HttpResponse('Hello, Company!')

def create_job_offer(request, obj_id=-1): #creating new and editing existing job offers
	# no input requirements for get
	# needs correct value for each key of get-response for post
	# if not request.user.is_authenticated:
	# 	return HttpResponse('Unauthorized', status=401)

	if obj_id > 0:
		jo = JobOffer.objects.filter(id=obj_id).first()
		if not jo:
			return HttpResponse('Vacature niet gevonden: ' + str(obj_id), status=404)
	else:
		jo = None

	# if not request.user.companyuser or not request.user.companyuser == jo.company:
	# 	return HttpResponse('Forbidden', status=403)

	form = CreateJobOfferForm(request.POST or None, instance=jo)
	if request.method == 'POST' and form.is_valid():
		obj = form.save(commit=False)
		obj.company = request.user.companyuser
		obj.save()
		return HttpResponse(json.dumps({'id': obj.id}), content_type='application/json')

	return HttpResponse(json.dumps(form_to_json(form)), content_type='application/json')

def get_skill_types(request):
	# no input requirements
	skills = SkillType.objects.all()
	return HttpResponse(json.dumps(list(map(lambda x: {"name": x.name, "id": x.id}, skills))), content_type='application/json')

def get_matching_skills(request):
	# needs 'type' (id of skilltype) and/or 'name' (string matching) in post keys. Can do without but will return all skills
	if not request.method == 'POST':
		return HttpResponse('Bad request', status=400)
	js = JobSkill.objects.all()
	if 'type' in request.POST and request.POST['type']:
		js = js.filter(type_of_skill_id=request.POST['type'])
	if 'name' in request.POST and request.POST['name']:
		js = js.filter(name__icontains=request.POST['name'])
	return HttpResponse(json.dumps(list(map(lambda x: {"name": x.name, "id": x.id}, js))), content_type='application/json')

def add_job_skills(request, offerid):
	# needs 'skill' (id of jobskill) and 'experience' (0-5)
	jo = JobOffer.objects.filter(id=offerid).first()
	if not jo:
		return HttpResponse('Vacature niet gevonden: ' + str(offerid), status=404)

	# if not request.user.companyuser or not request.user.companyuser == jo.company:
	# 	return HttpResponse('Forbidden', status=403)

	if not ('skill' in request.POST and request.POST['skill'] and JobSkill.objects.filter(id=request.POST['skill'])):
		return HttpResponse('Please provide a skill', status=400)
	js = JobSkill.objects.filter(id=request.POST['skill']).first()
	if not ('experience' in request.POST and request.POST['experience'] and 0 <= request.POST['experience'] <= 5):
		return HttpResponse('Please provide an experience', status=400)
	exp = int(request.POST['experience'])

	rs, _ = RequiredSkill.objects.get_or_create(offer_id=offerid, skill=js, defaults={'experience': exp})
	rs.experience = exp
	rs.save()

	return HttpResponse(json.dumps({'id': rs.id}), content_type='application/json')


def form_to_json(form):
	import django
	res = dict()
	for name, f in form.fields.items():
		res[name] = {
			# "widget": str(form[name]),
			"value": form[name].value(),
			"errs": list(map(lambda x: x.message, form[name].errors.as_data())),
		}
		if isinstance(form[name].field.widget, django.forms.widgets.Select):
			res['options'] = list(map(lambda x: x.data, form[name].subwidgets))
	return res
