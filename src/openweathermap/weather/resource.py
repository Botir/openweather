from import_export import resources, fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from .models import Sources, Cities

class SourceResource(resources.ModelResource):
    city = fields.Field(
        column_name='City',
        attribute='city',
        widget=ForeignKeyWidget(Cities, 'name'))
    day_obj = fields.Field(
        column_name='Date',
        attribute='day_obj',
        widget=DateTimeWidget("%Y-%m-%d %H:%M:%S"))
    temperature = Field(column_name='Temperature',)
    temperature_min = Field(column_name='Temperature (min)', )
    temperature_max = Field(column_name='Temperature (max)', )
    description = Field(column_name='Description', )
    feels_like = Field(column_name='Feels Like', )

    class Meta:
        model = Sources
        fields = ('dt',)

    def dehydrate_temperature(self, model):
        return model.content['temperature']

    def dehydrate_temperature_min(self, model):
        return model.content['temperature_min']

    def dehydrate_temperature_max(self, model):
        return model.content['temperature_max']

    def dehydrate_description(self, model):
        return model.content['description']

    def dehydrate_feels_like(self, model):
        return model.content['feels_like']
