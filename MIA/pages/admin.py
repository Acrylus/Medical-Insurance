from django.contrib import admin
from .models import Member, Provider, Coverage, Nurse

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'relation', 'patient_id', 'eligibility', 'effective_date', 'termination_date', 'ssn', 'address', 'accumulations', 'phone_number')
    list_filter = ('relation', 'eligibility')
    search_fields = ('first_name', 'last_name', 'patient_id', 'ssn')

admin.site.register(Member, MemberAdmin)

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('npi', 'name', 'phoneNumber')
    search_fields = ('name', 'npi')

admin.site.register(Provider, ProviderAdmin)

class CoverageAdmin(admin.ModelAdmin):
    list_display = ('service', 'coverage', 'after_deductible', 'copay', 'cpt_codes')
    search_fields = ('cpt_codes', 'coverage')

admin.site.register(Coverage, CoverageAdmin)

class NurseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'patient_name')

admin.site.register(Nurse, NurseAdmin)