# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from vacancies.models import ContactPerson, Location, Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):

    save_as = True

    list_display = (
        'title',
        'slug',
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

    filter_horizontal = (
        'locations',
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    fieldsets = (
        (_('Base Data'), {'classes': ('collapse',), 'fields': (
            'is_public',
            'title',
            'contact_person',
            'description',
            ('earliest_start', 'latest_start'),
        )}),
        (_('Qualifications & Requirements'), {'classes': ('collapse',), 'fields': (
            'work_experience',
            'management_responsibility',
            'max_distance',
        )}),
        (_('Conditions'), {'classes': ('collapse',), 'fields': (
            ('tariff_commitment', 'marginal_employment'),
            'social_insurance_employment',
            'collective_agreement',
            'compensation',
            'temporary_for_month',
            'limited_to',
        )}),
        (_('Working hours'), {'classes': ('collapse',), 'fields': (
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
        (_('Locations'), {'classes': ('collapse',), 'fields': (
            'locations',
        )}),
        (_('Meta data'), {'classes': ('collapse',), 'fields': (
            'suitable_to_support_the_integration_of_immigrants',
            'available_positions',
            'box_number',
            'slug',
        )}),
        (_('Alternative representations'), {'classes': ('collapse',), 'fields': (
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


@admin.register(ContactPerson)
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
            ('company_name', 'position'),
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


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display = (
        'label',
        'street',
        'zip_code',
        'city',
        'country',
    )

    list_filter = (
        'city',
    )

    fieldsets = (
        (None, {'fields': (
            'label',
            'street',
            'zip_code',
            'city',
            'country',
        )}),
    )
