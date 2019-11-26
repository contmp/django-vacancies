Vacancies
=========

Vacancies is a simple Django app to publish Web-based vacancies :)
For each vacancy, editors can choose between a various number of attributes.

Detailed documentation is in the "docs" directory - one day

Quick start
-----------

1. Add "vacancies" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'vacancies',
    ]

2. Include the vacancies URLconf in your project urls.py like this::

    path('vacancies/', include('vacancies.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/vacancies/ to view your wonderful vacancies.
