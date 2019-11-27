# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from vacancies.storage import contact_person_image


class ContactPerson(models.Model):

    SALUTATION_MRS = 1
    SALUTATION_MR = 2
    SALUTATION_CHOICES = (
        (SALUTATION_MRS, _('Mrs')),
        (SALUTATION_MR, _('Mr')),
    )

    company_name = models.CharField(max_length=255, blank=True, verbose_name=_('Company Name'))
    email = models.EmailField(blank=True, verbose_name=_('Email'))
    fax = models.CharField(max_length=255, blank=True, verbose_name=_('Fax'))
    first_name = models.CharField(max_length=255, blank=True, verbose_name=_('First name'))
    image = models.ImageField(upload_to=contact_person_image, null=True, blank=True, verbose_name=_('Image'))
    last_name = models.CharField(max_length=255, blank=True, verbose_name=_('Last name'))
    mobile = models.CharField(max_length=255, blank=True, verbose_name=_('Mobile'))
    name = models.CharField(max_length=255, blank=True, verbose_name=_('First name'))
    phone = models.CharField(max_length=255, blank=True, verbose_name=_('Phone'))
    position = models.CharField(max_length=255, blank=True, verbose_name=_('Position'))
    salutation = models.PositiveSmallIntegerField(choices=SALUTATION_CHOICES, default=SALUTATION_MRS, verbose_name=_('Salutation'))

    class Meta:
        verbose_name = _('Contact person')
        verbose_name_plural = _('Contact persons')

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return '%s %s %s'.strip() % (self.get_salutation_display(), self.first_name, self.last_name)

        return '%s' % self.pk
    full_name.fget.short_description = _('Full name')
