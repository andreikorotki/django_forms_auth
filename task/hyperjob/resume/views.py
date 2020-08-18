from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.views.generic import CreateView
from django import forms
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from .models import Resume


# Create your views here.
def menu(request):
    return render(request, 'menu.html')


def resumes(request):
    template_name = 'resumes.html'
    resumes_list = Resume.objects.all()
    return render(request, template_name, {'resumes': resumes_list})


class MyLoginView(LoginView):
    form = AuthenticationForm
    redirect_authenticated_user = True
    success_url = '/'
    template_name = 'login.html'

    def get_success_url(self):
        return '/'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


def logout_view(request):
    logout(request)
    return render(request, 'login.html')


class ResumeForm(forms.Form):
    description = forms.CharField(label='Resume Description', max_length='1024')


def newresume(request):
    # if this is a POST request we need to process the form data
    if request.user.is_authenticated and not request.user.is_staff:
        if request.method == 'POST':
            resume_form = ResumeForm(request.POST)
            if resume_form.is_valid():
                data = resume_form.cleaned_data  # data is a regular dictionary
                # user = User.objects.get(username=data.user.username)
                resume = Resume.objects.create(description=data.get("description"),
                                               author=request.user)
                return HttpResponseRedirect('/')

        # if a GET (or any other method) we'll create a blank form
        else:
            resume_form = ResumeForm()
    else:
        raise PermissionDenied

    return render(request, 'newresume.html', {'resume_form': resume_form})


def profilepage(request):
    return render(request, 'home.html')

# user = User.objects.get(username='AndreiK').update(is_staff=True)
