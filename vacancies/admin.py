# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from core.admin import site
from vacancies import models


@admin.register(models.Vacancy, site=site)
class VacancyAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'earliest_start',
        'hours_per_week',
        'is_public',
    )

    list_filter = (
        'is_public',
    )

    readonly_fields = (
        'image_preview',
    )

    fieldsets = (
        (None, {'fields': (
            'is_public',
            'title',
            'contact_person',
            'description',
            ('earliest_start', 'latest_start'),
        )}),
        (_('Qualifications & Requirements'), {'classes': ('_collapse',), 'fields': (
            'work_experience',
            'management_responsibility',
            'max_distance',
        )}),
        (_('Conditions'), {'classes': ('_collapse',), 'fields': (
            ('tariff_commitment', 'marginal_employment'),
            'social_insurance_employment',
            'collective_agreement',
            'compensation',
            'temporary_for_month',
            'limited_to',
        )}),
        (_('Working hours'), {'classes': ('_collapse',), 'fields': (
            (
                'working_hours_part_time_flexible',
                'working_hours_part_time_shift',
                'working_hours_part_time_morning',
                'working_hours_part_time_afternoon',
                'working_hours_part_time_eve',
                'working_hours_full_time',
                'working_hours_shift',
                'working_hours_night_work',
                'working_hours_weekend',
                'working_hours_telework',
            ),
            'hours_per_week',
            'additional_working_hours_information',
        )}),
        (_('Meta data'), {'classes': ('_collapse',), 'fields': (
            'suitable_to_support_the_integration_of_immigrants',
            'available_positions',
            'box_number',
        )}),
        (_('Alternative representations'), {'classes': ('_collapse',), 'fields': (
            'image_preview',
            'image',
            'pdf_version',
        )}),
    )

    def image_preview(self, contact_person):
        if not contact_person.image:
            return ''

        return mark_safe(u'<a href="%s" target="_blank" class="profileImage"><img src="%s" height="32"></a>' % (
            contact_person.image.url,
            contact_person.image.url,
        ))
    image_preview.short_description = _('Image preview')

    class Media:
        css = {
            'all': ('vacancies/css/admin.css',)
        }


@admin.register(models.ContactPerson, site=site)
class ContactPersonAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'email',
        'phone',
        'mobile',
        'image_preview',
    )

    list_filter = (
        'salutation',
    )

    readonly_fields = (
        'full_name',
        'image_preview',
    )

    fieldsets = (
        (None, {'fields': (
            'image_preview',
            'salutation',
            ('first_name', 'last_name'),
            ('phone', 'mobile'),
            ('email', 'fax'),
            'image',
        )}),
    )

    def image_preview(self, contact_person):
        if not contact_person.image:
            return ''

        return mark_safe(u'<a href="%s" target="_blank" class="profileImage"><img src="%s" height="32"></a>' % (
            contact_person.image.url,
            contact_person.image.url,
        ))
    image_preview.short_description = _('Image preview')

    class Media:
        css = {
            'all': ('vacancies/css/admin.css',)
        }
