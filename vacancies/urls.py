# -*- coding: utf-8 -*-
from django.urls import path
from vacancies.views import VacancyList, VacancyDetailView

app_name = 'vacancies'

urlpatterns = [
    path('', VacancyList.as_view(), name='index'),
    path('<slug:slug>/', VacancyDetailView.as_view(), name='detail'),
]
