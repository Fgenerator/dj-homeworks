from django.contrib import admin

from .models import Station, Route


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'name', 'get_routes')


class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)