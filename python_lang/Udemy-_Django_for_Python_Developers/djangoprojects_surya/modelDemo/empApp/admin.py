from django.contrib import admin
from empApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'salary']

admin.site.register(model_or_iterable=Employee, admin_class=EmployeeAdmin)
