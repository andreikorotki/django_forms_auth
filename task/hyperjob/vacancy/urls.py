from django.urls import path
from . import views

urlpatterns = [path('vacancies', views.vacancies),
               path('vacancy/new', views.newvacancy),
               ]
