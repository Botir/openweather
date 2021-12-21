from datetime import datetime, timedelta
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from .serializers import SourceSerializer
from openweathermap.weather.models import Sources, Cities


class SourcesView(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = SourceSerializer
    filter_fields = ('city', )

    def get_queryset(self):
        city = self.request.query_params.get('city')

        if city:
            try:
                city_model = Cities.objects.filter(name=city)[0:1].get()
            except Cities.DoesNotExist:
                return []
            qs = Sources.objects.filter(city=city_model.id)
            period = self.request.query_params.get('period')
            curr_date = datetime.today()
            daystart = datetime(year=curr_date.year, month=curr_date.month,
                                day=curr_date.day, hour=0, second=0)

            if period == 'weekly':
                end_date = curr_date + timedelta(weeks=1)
                qs2 = qs.filter(day_obj__range=(daystart, end_date))
            elif period == 'monthly':
                end_date = curr_date + timedelta(days=30)
                qs2 = qs.filter(day_obj__range=(daystart, end_date))
            else:
                qs2 = qs.filter(day_obj__startswith=daystart.date())
            return qs2
        else:
            return []
