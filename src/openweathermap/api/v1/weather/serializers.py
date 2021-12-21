from rest_framework import serializers

from openweathermap.weather.models import Sources


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sources
        fields = ['id', 'city', 'day_obj', 'content']
        read_only_fields = ['id', ]

