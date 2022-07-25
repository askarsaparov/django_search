from django.contrib import admin

from cities.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')


admin.site.register(City, CityAdmin)
