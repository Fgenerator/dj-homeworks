from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from app.readers import read_csv

DATA = read_csv(settings.BUS_STATION_CSV)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    paginator = Paginator(DATA, 10)
    current_page = int(request.GET.get('page', 1))
    stations = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if stations.has_previous():
        prev_page = stations.previous_page_number()
    if stations.has_next():
        next_page = stations.next_page_number()
    # current_page = 1
    # next_page_url = 'write your url'
    return render_to_response('index.html', context={
        # 'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })

