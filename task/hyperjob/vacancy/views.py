from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from .models import Vacancy


def vacancies(request):
    template_name = 'vacancies.html'
    vacancies_list = Vacancy.objects.all()
    return render(request, template_name, {'vacancies': vacancies_list})


class VacancyForm(forms.Form):
    description = forms.CharField(label='Vacancy Description', max_length='1024')


def newvacancy(request):
    # if this is a POST request we need to process the form data
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            vacancy_form = VacancyForm(request.POST)
            if vacancy_form.is_valid():
                data = vacancy_form.cleaned_data  # data is a regular dictionary
                vacancy = Vacancy.objects.create(description=data.get("description"),
                                               author=request.user)
                return HttpResponseRedirect('/')

        # if a GET (or any other method) we'll create a blank form
        else:
            vacancy_form = VacancyForm()
    else:
        raise PermissionDenied

    return render(request, 'newvacancy.html', {'vacancy_form': vacancy_form})

