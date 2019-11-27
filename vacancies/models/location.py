# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):

    label = models.CharField(max_length=255, blank=True, verbose_name=_('Label'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    country = models.CharField(max_length=100, blank=True, verbose_name=_('Country'))
    street = models.CharField(max_length=100, blank=True, verbose_name=_('Street'))
    zip_code = models.CharField(max_length=25, blank=True, verbose_name=_('Zip Code'))

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        if self.label:
            return self.label

        return '%s %s %s'.strip() % (
            self.street,
            self.zip_code,
            self.city,
        )
