from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('inschrijven', views.signup, name='signup'),
	path('joboffer/create', views.create_job_offer, name='create_job_offer'),
	path('joboffer/edit/<int:obj_id>', views.create_job_offer, name='create_job_offer'),
]