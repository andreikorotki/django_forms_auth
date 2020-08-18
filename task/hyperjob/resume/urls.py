from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

from .views import MyLoginView
from .views import MySignupView
from . import views

urlpatterns = [
    path('', views.menu),
    path('home', views.profilepage),
    path('resumes', views.resumes),
    path('resume/new', views.newresume),
    path('signup', MySignupView.as_view()),
    path('login', MyLoginView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('logout', views.logout_view),
]
