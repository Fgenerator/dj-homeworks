from django.contrib import admin

from .models import Column, Data


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'serial_number')


class DataAdmin(admin.ModelAdmin):
    list_display = ('file_path',)


admin.site.register(Column, ColumnAdmin)
admin.site.register(Data, DataAdmin)