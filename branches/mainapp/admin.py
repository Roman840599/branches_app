from django.contrib import admin
from .models import Employee, Branch


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name')


admin.site.register(Branch)