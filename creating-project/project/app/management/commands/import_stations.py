import csv

from django.core.management.base import BaseCommand

from app.models import Station, Route

CSV_FILENAME = 'moscow_bus_stations.csv'


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(CSV_FILENAME, 'rt') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                print(row['Latitude_WGS84'], row['Longitude_WGS84'], row['Name'])
                print(row['RouteNumbers'].split(';'))
                station = Station(
                    latitude=row['Latitude_WGS84'],
                    longitude=row['Longitude_WGS84'],
                    name=row['Name'],
                )
                station.save()
                for route_name in row['RouteNumbers'].split(';'):
                    route, created = Route.objects.get_or_create(name=route_name)
                    station.routes.add(route)
