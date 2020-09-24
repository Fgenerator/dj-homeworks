from django.db import models


class Station(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    routes = models.ManyToManyField(
        'Route',
        related_name='stations',
        default=None
    )
    name = models.CharField(max_length=100)

    def get_routes(self):
        return " ".join([route.name for route in self.routes.all()])


class Route(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name