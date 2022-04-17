from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Month, Task


# Register your models here.
@admin.register(Month)
class MonthAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'number', 'order']


@admin.register(Task)
class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'description', 'status', 'month']
