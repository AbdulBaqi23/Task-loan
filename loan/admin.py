from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name','amount']

@admin.register(loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['requested_by','amount','taken_from','time','approved']