from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('offers/types', views.get_offer_types, name='get_offer_types'),
	path('offers/match', views.get_matching_offers, name='get_matching_offers'),
	path('companies/find', views.get_companies, name='get_companies'),
]