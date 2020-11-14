from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('inschrijven', views.signup, name='signup'),
	path('joboffer/create', views.create_job_offer, name='create_job_offer'),
	path('joboffer/edit/<int:obj_id>', views.create_job_offer, name='create_job_offer'),
	path('skills/add/<int:offerid>', views.add_job_skills, name='add_job_skills'),
	path('skills/types', views.get_skill_types, name='get_skill_types'),
	path('skills/match', views.get_matching_skills, name='get_matching_skills'),
]