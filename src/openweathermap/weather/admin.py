from django.contrib import admin
from django.contrib.admin.filters import RelatedFieldListFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from import_export.admin import ExportActionMixin
from .models import Cities, Sources
from .resource import SourceResource

class DropdownFilter(RelatedFieldListFilter):
    template = 'dropdown_filter.html'

class CityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'country']
    list_display = ("name", "state", "country", "server_id")
    list_display_links = ('name', 'server_id')


class SourceAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = SourceResource
    list_filter = (('city', DropdownFilter),
                   ('day_obj', DateRangeFilter)
                   )
    list_display = ("day_obj", "city", "temperature", "temperature_min", "temperature_min", "description",  "updated_dt")
    list_display_links = ('day_obj', )

    def temperature(self, instance):
        return instance.content['temperature']

    def temperature_min(self, instance):
        return instance.content['temperature_min']

    def description(self, instance):
        return instance.content['description']

admin.site.register(Cities, CityAdmin)
admin.site.register(Sources, SourceAdmin)
