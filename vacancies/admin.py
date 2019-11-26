# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core.admin import site
from vacancies import models


@admin.register(models.Vacancy, site=site)
class VacancyAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': (
            'marginal_employment',
            'suitable_to_support_the_integration_of_immigrants',
            'title',
            'box_number',
            'count',
            'contact_person',
            'description',
            'management_responsibility',
            ('earliest_start', 'latest_start'),
            'work_experience',
            'max_distance',
            'pdf_version',
        )}),
        (_('Conditions'), {'classes': ('collapse',), 'fields': (
            (
                'working_hours_part_time_flexible',
                'working_hours_part_time_shift',
                'working_hours_part_time_morning',
                'working_hours_part_time_afternoon',
                'working_hours_part_time_eve',
            ),
            (
                'working_hours_full_time',
                'working_hours_shift',
                'working_hours_night_work',
                'working_hours_weekend',
                'working_hours_telework',
            ),
            'hours_per_week',
            'social_insurance_employment',
            'additional_working_hours_information',
            ('collective_agreement', 'tariff_commitment'),
            'compensation',
            ('temporary_for_month', 'limited_to'),
        )}),
    )


@admin.register(models.ContactPerson, site=site)
class ContactPersonAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'mobile',
    )

    list_filter = (
        'salutation',
    )

    fieldsets = (
        (None, {'fields': (
            'salutation',
            ('first_name', 'last_name'),
            ('phone', 'mobile'),
            ('email', 'fax'),
        )}),
    )
