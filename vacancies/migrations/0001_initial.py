# Generated by Django 2.2 on 2019-11-27 02:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import vacancies.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255, verbose_name='Company Name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('fax', models.CharField(blank=True, max_length=255, verbose_name='Fax')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First name')),
                ('image', models.ImageField(blank=True, null=True, upload_to=vacancies.storage.contact_person_image, verbose_name='Image')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last name')),
                ('mobile', models.CharField(blank=True, max_length=255, verbose_name='Mobile')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='First name')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Phone')),
                ('position', models.CharField(blank=True, max_length=255, verbose_name='Position')),
                ('salutation', models.PositiveSmallIntegerField(choices=[(1, 'Mrs'), (2, 'Mr')], default=1, verbose_name='Salutation')),
            ],
            options={
                'verbose_name': 'Contact person',
                'verbose_name_plural': 'Contact persons',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Label')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Country')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Street')),
                ('zip_code', models.CharField(blank=True, max_length=25, verbose_name='Zip Code')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_working_hours_information', models.TextField(blank=True, verbose_name='Additional working hours information')),
                ('available_positions', models.IntegerField(blank=True, default=1, null=True, verbose_name='Available positions')),
                ('box_number', models.CharField(blank=True, max_length=255, verbose_name='Box Number')),
                ('collective_agreement', models.CharField(blank=True, max_length=255, verbose_name='Collective agreement')),
                ('compensation', models.CharField(blank=True, max_length=255, verbose_name='Compensation')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('earliest_start', models.DateField(blank=True, null=True, verbose_name='Earliest start')),
                ('hours_per_week', models.IntegerField(blank=True, null=True, verbose_name='Hours per week')),
                ('image', models.ImageField(blank=True, null=True, upload_to=vacancies.storage.vacancy_image, verbose_name='Image')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
                ('latest_start', models.DateField(blank=True, null=True, verbose_name='Latest start')),
                ('limited_to', models.DateField(blank=True, null=True, verbose_name='Limited to')),
                ('management_responsibility', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'No management responsibility'), (2, 'All management levels'), (3, 'Team management, project management, group management'), (4, 'Head of Department, Division Management, Department Management'), (5, 'Management, board, management'), (6, 'Staff function')], null=True, verbose_name='Management responsibility')),
                ('marginal_employment', models.BooleanField(default=False, verbose_name='Marginal employment')),
                ('max_distance', models.IntegerField(blank=True, help_text='km/miles', null=True, verbose_name='Max Distance')),
                ('pdf_version', models.FileField(blank=True, null=True, upload_to=vacancies.storage.vacancy_pdf, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Pdf version')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('social_insurance_employment', models.BooleanField(null=True, verbose_name='Social insurance employment')),
                ('suitable_to_support_the_integration_of_immigrants', models.BooleanField(default=False, verbose_name='Suitable to support the integration of immigrants')),
                ('tariff_commitment', models.BooleanField(default=False, verbose_name='Tariff commitment')),
                ('temporary_for_month', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Temporary for month')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('work_experience', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Entry level'), (2, 'With professional experience')], null=True, verbose_name='Work experience')),
                ('working_hours_full_time', models.BooleanField(default=False, verbose_name='Full time')),
                ('working_hours_night_work', models.BooleanField(default=False, verbose_name='Night work')),
                ('working_hours_part_time_afternoon', models.BooleanField(default=False, verbose_name='Part time (afternoon)')),
                ('working_hours_part_time_eve', models.BooleanField(default=False, verbose_name='Part time (eve)')),
                ('working_hours_part_time_flexible', models.BooleanField(default=False, verbose_name='Part time (flexible)')),
                ('working_hours_part_time_morning', models.BooleanField(default=False, verbose_name='Part time (morning)')),
                ('working_hours_part_time_shift', models.BooleanField(default=False, verbose_name='Part time (shift)')),
                ('working_hours_shift', models.BooleanField(default=False, verbose_name='Shift')),
                ('working_hours_telework', models.BooleanField(default=False, verbose_name='Telework')),
                ('working_hours_weekend', models.BooleanField(default=False, verbose_name='Weekend')),
                ('contact_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_offers', to='vacancies.ContactPerson', verbose_name='Contact Person')),
                ('locations', models.ManyToManyField(blank=True, related_name='vacancies', to='vacancies.Location', verbose_name='Locations')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
            },
        ),
    ]
