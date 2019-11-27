# -*- coding: utf-8 -*-
from django.utils.text import slugify


def generate_unique_slug(klass, field):

    origin_slug = slugify(field)
    unique_slug = origin_slug
    loop_interval = 1

    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, loop_interval)
        loop_interval += 1

    return unique_slug
