# Generated by Django 4.2.5 on 2023-10-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('relation', models.CharField(max_length=30)),
                ('patient_id', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('effective_date', models.DateField()),
                ('termination_date', models.DateField()),
                ('ssn', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('accumulations', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
    ]
