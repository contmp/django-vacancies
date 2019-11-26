# -*- coding: utf-8 -*-
import os
import uuid
import hashlib
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


def get_image_destination(instance, filename):
    model_name = ('%s' % instance.__class__.__name__).lower()
    _, ext = os.path.splitext(filename)
    uu = hashlib.md5(instance.image.read()).hexdigest()
    return '/'.join([model_name, uu[:2], uu[2:4], uu, slugify(instance.name) + ext.lower()])


class ContactPerson(models.Model):

    SALUTATION_MRS = 1
    SALUTATION_MR = 2
    SALUTATION_CHOICES = (
        (SALUTATION_MRS, _('Mrs')),
        (SALUTATION_MR, _('Mr')),
    )

    email = models.EmailField(blank=True, verbose_name=_('Email'))
    fax = models.CharField(max_length=255, blank=True, verbose_name=_('Fax'))
    first_name = models.CharField(max_length=255, blank=True, verbose_name=_('First name'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=get_image_destination, null=True, blank=True, verbose_name=_('Image'))
    last_name = models.CharField(max_length=255, blank=True, verbose_name=_('Last name'))
    mobile = models.CharField(max_length=255, blank=True, verbose_name=_('Mobile'))
    name = models.CharField(max_length=255, blank=True, verbose_name=_('First name'))
    phone = models.CharField(max_length=255, blank=True, verbose_name=_('Phone'))
    salutation = models.PositiveSmallIntegerField(choices=SALUTATION_CHOICES, default=SALUTATION_MRS, verbose_name=_('Salutation'))

    class Meta:
        verbose_name = _('Contact person')
        verbose_name_plural = _('Contact persons')

    def __str__(self):

        if self.first_name and self.last_name:
            return '%s %s'.strip() % (self.first_name, self.last_name)

        return '%s' % self.pk
