# -*- coding: utf-8 -*-
import os
import hashlib
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


def get_pdf_destination(instance, filename):
    uu = hashlib.md5(instance.pdf_version.read()).hexdigest()
    return '/'.join(['joboffers', uu[:2], uu[2:4], uu[4:8], uu + '.pdf'])


def get_image_destination(instance, filename):
    model_name = ('%s' % instance.__class__.__name__).lower()
    _, ext = os.path.splitext(filename)
    uu = hashlib.md5(instance.image.read()).hexdigest()
    return '/'.join([model_name, uu[:2], uu[2:4], uu, slugify(instance.name) + ext.lower()])


class Vacancy(models.Model):

    MANAGEMENT_RESPONSIBILITY_NONE = 1
    MANAGEMENT_RESPONSIBILITY_ALL = 2
    MANAGEMENT_RESPONSIBILITY_TEAM = 3
    MANAGEMENT_RESPONSIBILITY_DEPARTMENT = 4
    MANAGEMENT_RESPONSIBILITY_BOARD = 5
    MANAGEMENT_RESPONSIBILITY_STAFF = 6
    MANAGEMENT_RESPONSIBILITY_CHOICES = (
        (MANAGEMENT_RESPONSIBILITY_NONE, _('No management responsibility')),
        (MANAGEMENT_RESPONSIBILITY_ALL, _('All management levels')),
        (MANAGEMENT_RESPONSIBILITY_TEAM, _('Team management, project management, group management')),
        (MANAGEMENT_RESPONSIBILITY_DEPARTMENT, _('Head of Department, Division Management, Department Management')),
        (MANAGEMENT_RESPONSIBILITY_BOARD, _('Management, board, management')),
        (MANAGEMENT_RESPONSIBILITY_STAFF, _('Staff function')),
    )

    WORK_EXPERIENCE_ENTRY = 1
    WORK_EXPERIENCE_EXPERIENCE = 2
    WORK_EXPERIENCE_CHOICES = (
        (WORK_EXPERIENCE_ENTRY, _('Entry level')),
        (WORK_EXPERIENCE_EXPERIENCE, _('With professional experience')),
    )

    additional_working_hours_information = models.TextField(blank=True, verbose_name=_('Additional working hours information'))
    box_number = models.CharField(max_length=255, blank=True, verbose_name=_('Box Number'))
    collective_agreement = models.CharField(max_length=255, blank=True, verbose_name=_('Collective agreement'))
    compensation = models.CharField(max_length=255, blank=True, verbose_name=_('Compensation'))
    contact_person = models.ForeignKey('ContactPerson', null=True, blank=True, on_delete=models.SET_NULL, related_name='job_offers', verbose_name=_('Contact Person'))
    count = models.IntegerField(default=1, verbose_name=_('Count'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    earliest_start = models.DateField(blank=True, null=True, verbose_name=_('Earliest start'))
    hours_per_week = models.IntegerField(blank=True, null=True, verbose_name=_('Hours per week'))
    image = models.ImageField(upload_to=get_image_destination, null=True, blank=True, verbose_name=_('Image'))
    latest_start = models.DateField(blank=True, null=True, verbose_name=_('Latest start'))
    limited_to = models.DateField(blank=True, null=True, verbose_name=_('Limited to'))
    management_responsibility = models.PositiveSmallIntegerField(choices=MANAGEMENT_RESPONSIBILITY_CHOICES, blank=True, null=True, verbose_name=_('Management responsibility'))
    marginal_employment = models.BooleanField(default=False, verbose_name=_('Marginal employment'))
    max_distance = models.IntegerField(blank=True, null=True, verbose_name=_('Max Distance'))
    pdf_version = models.FileField(blank=True, null=True, upload_to=get_pdf_destination, validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name=_('Pdf'))
    social_insurance_employment = models.BooleanField(null=True, verbose_name=_('Social insurance employment'))
    suitable_to_support_the_integration_of_immigrants = models.BooleanField(default=False, verbose_name=_('Suitable to support the integration of immigrants'))
    tariff_commitment = models.BooleanField(default=False, verbose_name=_('Tariff commitment'))
    temporary_for_month = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_('Temporary for month'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    work_experience = models.PositiveSmallIntegerField(choices=WORK_EXPERIENCE_CHOICES, blank=True, null=True, verbose_name=_('Work experience'))
    working_hours_full_time = models.BooleanField(default=False, verbose_name=_('Full time'))
    working_hours_night_work = models.BooleanField(default=False, verbose_name=_('Night work'))
    working_hours_part_time_afternoon = models.BooleanField(default=False, verbose_name=_('Part time (afternoon)'))
    working_hours_part_time_eve = models.BooleanField(default=False, verbose_name=_('Part time (eve)'))
    working_hours_part_time_flexible = models.BooleanField(default=False, verbose_name=_('Part time (flexible)'))
    working_hours_part_time_morning = models.BooleanField(default=False, verbose_name=_('Part time (morning)'))
    working_hours_part_time_shift = models.BooleanField(default=False, verbose_name=_('Part time (shift)'))
    working_hours_shift = models.BooleanField(default=False, verbose_name=_('Shift'))
    working_hours_telework = models.BooleanField(default=False, verbose_name=_('Telework'))
    working_hours_weekend = models.BooleanField(default=False, verbose_name=_('Weekend'))

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')
