from django.db import models

from model_utils.models import TimeStampedModel
class CityWeather(TimeStampedModel):
    name = models.CharField(max_length=25, verbose_name='Name')
    celcius = models.IntegerField(verbose_name='Celcius')
    time_rain = models.IntegerField(verbose_name='Rain')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['-created']
