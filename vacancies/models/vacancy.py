# -*- coding: utf-8 -*-
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from vacancies.storage import vacancy_pdf, vacancy_image
from vacancies.utils import generate_unique_slug


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
    available_positions = models.IntegerField(default=1, blank=True, null=True, verbose_name=_('Available positions'))
    box_number = models.CharField(max_length=255, blank=True, verbose_name=_('Box Number'))
    collective_agreement = models.CharField(max_length=255, blank=True, verbose_name=_('Collective agreement'))
    compensation = models.CharField(max_length=255, blank=True, verbose_name=_('Compensation'))
    contact_person = models.ForeignKey('ContactPerson', null=True, blank=True, on_delete=models.SET_NULL, related_name='job_offers', verbose_name=_('Contact Person'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    earliest_start = models.DateField(blank=True, null=True, verbose_name=_('Earliest start'))
    hours_per_week = models.IntegerField(blank=True, null=True, verbose_name=_('Hours per week'))
    image = models.ImageField(upload_to=vacancy_image, null=True, blank=True, verbose_name=_('Image'))
    is_public = models.BooleanField(default=False, verbose_name=_('Is public'))
    latest_start = models.DateField(blank=True, null=True, verbose_name=_('Latest start'))
    limited_to = models.DateField(blank=True, null=True, verbose_name=_('Limited to'))
    locations = models.ManyToManyField('Location', blank=True, related_name='vacancies', verbose_name=_('Locations'))
    management_responsibility = models.PositiveSmallIntegerField(choices=MANAGEMENT_RESPONSIBILITY_CHOICES, blank=True, null=True, verbose_name=_('Management responsibility'))
    marginal_employment = models.BooleanField(default=False, verbose_name=_('Marginal employment'))
    max_distance = models.IntegerField(blank=True, null=True, help_text=_('km/miles'), verbose_name=_('Max Distance'))
    pdf_version = models.FileField(blank=True, null=True, upload_to=vacancy_pdf, validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name=_('Pdf version'))
    slug = models.SlugField(max_length=250, unique=True)
    social_insurance_employment = models.BooleanField(null=True, verbose_name=_('Social insurance employment'))
    suitable_to_support_the_integration_of_immigrants = models.BooleanField(default=False, verbose_name=_('Suitable to support the integration of immigrants'))
    tariff_commitment = models.BooleanField(default=False, verbose_name=_('Tariff commitment'))
    temporary_for_month = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_('Temporary for month'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vacancy-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = generate_unique_slug(Vacancy, self.title)

        super().save(*args, **kwargs)
