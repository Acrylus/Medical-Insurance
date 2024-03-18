from django import forms
from django.contrib.auth.models import User
from .models import Member, Provider, Coverage, Nurse
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import SelectDateWidget


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class AddMemberForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=SelectDateWidget(
            years=range(1900, 3000)  # Adjust the range of years as needed
        ),
        help_text='Required. Enter your date of birth.'
    )

    effective_date = forms.DateField(
        widget=SelectDateWidget(
            years=range(1900, 3000)  # Adjust the range of years as needed
        ),
        help_text='Required. Enter your date of birth.'
    )


    termination_date = forms.DateField(
        widget=SelectDateWidget(
            years=range(1900, 3000)  # Adjust the range of years as needed
        ),
        help_text='Required. Enter your date of birth.'
    )

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'date_of_birth', 
                  'relation', 'patient_id', 'eligibility', 'effective_date', 'termination_date', 
                  'ssn', 'address', 'accumulations', 'phone_number']

class SearchForm(forms.Form):
    searchType = forms.ChoiceField(
        choices=[("patientID", "Patient ID"), ("ssn", "SSN")],
        widget=forms.Select(attrs={"required": "required"})
    )
    searchValue = forms.CharField(required=True)

class EditMemberForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=SelectDateWidget(
            years=range(1900, 3000)
        ),
        help_text='Required. Enter the date of birth.'
    )
    
    effective_date = forms.DateField(
        widget=SelectDateWidget(
            years=range(1900, 3000)  # Adjust the range of years as needed
        ),
        help_text='Required. Enter your date of birth.'
    )

    termination_date = forms.DateField(
        widget=SelectDateWidget(
            years=range(1900, 3000)  # Adjust the range of years as needed
        ),
        help_text='Required. Enter your date of birth.'
    )

    # Add other fields as needed

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'date_of_birth', 'relation', 'patient_id', 
                  'eligibility', 'ssn', 'address', 'accumulations', 'phone_number']

class AddProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['npi', 'name', 'phoneNumber']

class EditProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['npi', 'name', 'phoneNumber']

class AddCoverageForm(forms.ModelForm):
    class Meta:
        model = Coverage
        fields = ['service', 'coverage', 'after_deductible', 'copay', 'cpt_codes']

class EditCoverageForm(forms.ModelForm):
    class Meta:
        model = Coverage
        fields = ['service', 'coverage', 'after_deductible', 'copay', 'cpt_codes']

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['name', 'patient_name']