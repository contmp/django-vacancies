Develop:

```sh
vv
pip install django
# Create / Update locales
mkdir vacancies/locale/NEW_LOCALE
cd vacancies
django-admin makemessages --ignore=.virtualenv/* --ignore=fixtures/* --ignore=assets/* -a --no-location -e html,pug,py,txt
# django-admin compilemessages

python setup.py sdist
# Inside Dev Project Apps Dir:
ln -s  ../../django-vacancies/vacancies
# Or:
pip install --user django-vacancies/dist/django-vacancies-0.1.tar.gz
pip install --user ~/Repositories/nadobit/blueprints/django-vacancies/dist/django-vacancies-0.1.tar.gz
pip uninstall django-vacancies
```


Credits:
https://docs.djangoproject.com/en/2.2/intro/reusable-apps/
