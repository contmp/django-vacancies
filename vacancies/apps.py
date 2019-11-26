# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class VacanciesConfig(AppConfig):
    name = 'vacancies'
    verbose_name = _('Vacancies Config')
