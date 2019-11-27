# -*- coding: utf-8 -*-
from django.urls import path
from vacancies.views import VacancyList, VacancyDetailView


urlpatterns = [
    path('', VacancyList.as_view(), name='vacancy-index'),
    path('<slug:slug>/', VacancyDetailView.as_view(), name='vacancy-detail'),
]
