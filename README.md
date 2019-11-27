# Vacancies

Vacancies is a simple Django app to publish Web-based vacancies :)
For each vacancy, editors can choose between a various number of attributes.

Detailed documentation is in the "docs" directory - one day

## Quick start

```
1. Add "vacancies" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'vacancies',
        # or
        'vacancies.apps.VacanciesConfig', # <- prefered for localized app name
    ]

2. Include the vacancies URLconf in your project urls.py like this::

    path('vacancies/', include('vacancies.urls')),

3. Run `python manage.py migrate` to create the vacancies models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a vacancy (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/vacancies/ to view your wonderful vacancies.
```

## Admin Integration

By default django admin autodiscover is beeing used. If you have custom admin
site, register the vacancies models by yourself e.g.:

```python
# project/admin.py
from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin, Group, GroupAdmin
from django.utils.translation import ugettext_lazy as _
.
.
.
from vacancies.admin import Vacancy, VacancyAdmin, ContactPerson, ContactPersonAdmin, Location, LocationAdmin


class AdminSite(admin.AdminSite):
    site_title = 'My cool Admin'
    site_header = _('Database Interface')
    index_title = _('Administration')

site = AdminSite()
site.register(User, UserAdmin)
site.register(Group, GroupAdmin)
.
.
.
site.register(Vacancy, VacancyAdmin)
site.register(ContactPerson, ContactPersonAdmin)
site.register(Location, LocationAdmin)

```

## Customize


You can create a __vacancies/vacancies_base.html__ Base Template to implement
you pug environemnt e.g.

```
# vacancies/vacancies_base.html
{% extends "base.pug" %}
```


## Development


### Contribute Locales

```sh
# Inside cloned repository folder:
mkdir .virtualenv && python3 -m venv .virtualenv && sv
pip install django
mkdir vacancies/locale/NEW_LOCALE
cd vacancies
django-admin makemessages --ignore=.virtualenv/* --ignore=fixtures/* --ignore=assets/* -a --no-location -e html,pug,py,txt
# Use Po-Edit or other editor to edit locales
```

### Package and Install Development Version

```sh
# Inside cloned repository folder:
python setup.py sdist

# Inside Dev Project Apps Dir:
ln -s  ../../django-vacancies/vacancies

# Or:
pip install --user django-vacancies/dist/django-vacancies-0.1.tar.gz
pip uninstall django-vacancies

```


Credits:
https://docs.djangoproject.com/en/2.2/intro/reusable-apps/
https://djangosnippets.org/snippets/10643/
