# -*- coding: utf-8 -*-
from django.urls import path
from vacancies.views import VacancyList, VacancyDetailView

urlpatterns = [
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<slug:slug>/', VacancyDetailView.as_view(), name='vacancy-detail'),
]
