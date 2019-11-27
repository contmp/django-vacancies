# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from vacancies.models import Vacancy


class VacancyList(ListView):
    queryset = Vacancy.objects.filter(is_public=True)
    context_object_name = 'public_vacancies'


class VacancyDetailView(DetailView):
    context_object_name = 'vacancy'
    queryset = Vacancy.objects.filter(is_public=True)
