from django.shortcuts import render
from django.http import HttpResponse

from companies.models import *
import json
# Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return HttpResponse('Unauthorized', status=401)
	return render(request, 'applicants/index.html', {})

def get_offer_types(request):
	# no input requirements
	offers = OfferType.objects.all()
	return HttpResponse(json.dumps(list(map(lambda x: {"name": x.name, "id": x.id}, offers))), content_type='application/json')

def get_matching_offers(request):
	# needs 'type' (id of offertype) and/or 'name' (string matching) and/or comapny in post keys. Can do without but will return all offers
	if not request.method == 'POST':
		return HttpResponse('Bad request', status=400)
	jo = JobOffer.objects.all()
	if 'type' in request.POST and request.POST['type']:
		jo = jo.filter(type_of_offer_id=request.POST['type'])
	if 'name' in request.POST and request.POST['name']:
		jo = jo.filter(name__icontains=request.POST['name'])
	if 'company' in request.POST and request.POST['company'] and CompanyUser.objects.filter(id=request.POST['comapny']):
		jo = jo.filter(company_id=request.POST['company'])
	return HttpResponse(json.dumps(list(map(lambda x: {"name": x.name, "id": x.id, "company": x.company, "desc": x.desc}, jo))), content_type='application/json')

def get_companies(request):
	cu = CompanyUser.objects.all()
	if 'name' in (request.POST or {}):
		cu = cu.filter(companyname__icontains=request.POST['name'])
	return HttpResponse(json.dumps(list(map(lambda x: {"name": x.companyname, "id": x.id}, cu))), content_type='application/json')
