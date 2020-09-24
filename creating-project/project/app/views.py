from django.shortcuts import render

from .models import Station, Route


def get_center():
    max_longitude = Station.objects.all().order_by('-longitude').first().longitude
    min_longitude = Station.objects.all().order_by('longitude').first().longitude

    max_latitude = Station.objects.all().order_by('-latitude').first().latitude
    min_latitude = Station.objects.all().order_by('latitude').first().latitude

    center_longitude = (max_longitude + min_longitude) / 2
    center_latitude = (max_latitude + min_latitude) / 2

    center = {
        'y': round(center_latitude, 2),
        'x': round(center_longitude, 2)
    }
    return center


def station_view(request):
    template = 'stations.html'

    route = request.GET.get('route')
    route_obj = Route.objects.get(name=route)

    stations = Station.objects.all()
    routes = Route.objects.all()

    context = {
        'stations': stations,
        'routes': routes,
        'route': route_obj,
        'center': get_center()
    }

    return render(request, template, context)
