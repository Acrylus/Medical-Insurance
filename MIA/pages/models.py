from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from django.db.models import DateField

# Create your models here.

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    date_of_birth = models.DateField(help_text='Required. Enter your date of birth')

    RELATION_CHOICES = [
        ('Policy Holder', 'Policy Holder'),
        ('Dependent Spouse', 'Dependent Spouse'),
        ('Dependent Daughter', 'Dependent Daughter'),
        ('Dependent Son', 'Dependent Son'),
    ]
    relation = models.CharField(max_length=30, choices=RELATION_CHOICES, verbose_name='Relation')
    
    patient_id = models.CharField(max_length=30, verbose_name='Patient ID')
    
    ELIGIBILITY_CHOICES = [
        ('Active', 'Active'),
        ('Terminated', 'Terminated'),
    ]
    eligibility = models.CharField(max_length=30, choices=ELIGIBILITY_CHOICES, verbose_name='Eligibility')
    
    effective_date = models.DateField(verbose_name='Effective Date')
    termination_date = models.DateField(verbose_name='Termination Date')
    
    ssn = models.CharField(max_length=30, verbose_name='SSN')
    address = models.CharField(max_length=100, verbose_name='Address')
    accumulations = models.CharField(max_length=30, verbose_name='Accumulations')
    phone_number = models.CharField(max_length=30, verbose_name='Phone Number')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Provider(models.Model):
    npi = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Coverage(models.Model):
    # Your Coverage model fields and definitions go here
    # For example:
    service = models.CharField(max_length=255)
    coverage = models.CharField(max_length=255)
    after_deductible = models.FloatField()
    copay = models.CharField(max_length=255)
    cpt_codes = models.CharField(max_length=255)

    def __str__(self):
        return self.service

class Nurse(models.Model):
    name = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.patient_name}"