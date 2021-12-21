from django.db import models
from django.db.models import JSONField

# Ob-havo uchun hududlar
class Cities(models.Model):
    id = models.AutoField(primary_key=True)

    # Bu openweathermap.org dagi city ID uchun.
    server_id = models.IntegerField(blank=False, null=False, unique=True)

    name = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)

    # Joylashgan nuqta koordinatasi
    coord = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

# Ob-Havo ma'lumotlari uchun
class Sources(models.Model):

    # WEATHER DATA FROM API
    content = JSONField(blank=False, null=False, default=dict)

    # Unix dt from DATA
    dt = models.IntegerField(blank=False, null=False,)

    # City Model
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name="cities")

    # weather datetime
    day_obj = models.DateTimeField(blank=False, null=False)

    # weather type (??)
    weather_type = models.SmallIntegerField(null=False, default=1)

    # system created or updated time
    created_dt = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, editable=False)
    updated_dt = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, editable=False)

    class Meta:
        unique_together = (('dt', 'city'))
        verbose_name = "Source"
        verbose_name_plural = "Sources"
