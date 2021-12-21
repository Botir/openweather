from django.urls import path
from .weather.views import SourcesView

urlpatterns = [
    path('weather/', SourcesView.as_view(), name='source-list'),
]
