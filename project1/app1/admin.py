from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['e_id', 'e_name','salary', 'city', 'c_name']
admin.site.register(Employee,EmployeeAdmin)