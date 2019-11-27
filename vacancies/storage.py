# -*- coding: utf-8 -*-
import os
import hashlib
from django.utils.text import slugify


def contact_person_image(instance, filename):
    _, ext = os.path.splitext(filename)
    uu = hashlib.md5(instance.image.read()).hexdigest()
    return '/'.join(['vacancies', 'contact_persons', uu[:2], uu[2:4], uu, slugify(instance.full_name) + ext.lower()])


def vacancy_pdf(instance, filename):
    uu = hashlib.md5(instance.pdf_version.read()).hexdigest()
    return '/'.join(['vacancies', 'pdf_versions', uu[:2], uu[2:4], uu[4:8], uu + '.pdf'])


def vacancy_image(instance, filename):
    _, ext = os.path.splitext(filename)
    uu = hashlib.md5(instance.image.read()).hexdigest()
    return '/'.join(['vacancies', 'images', uu[:2], uu[2:4], uu, slugify(instance.title) + ext.lower()])
