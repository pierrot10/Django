from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Fields, Stations, Sensors


class IndexView(generic.ListView):
    template_name = 'console/index.html'
    context_object_name = 'fields_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Fields.objects.order_by('-field_created')[:5]


# class FieldsView(generic.DetailView):
#    model = Fields
#    template_name = 'console/fields.html'


# class StationsView(generic.ListView):
#    model = Stations
#    context_object_name = 'stations_list'
#    template_name = 'console/stations.html'
#
#    def get_queryset(self):
#        """Return the last five published station."""
#         return Stations.objects.order_by('-station_created')[:10]

def stations(request, fields_id_field):
    #stations_list = get_object_or_404(Stations, pk=field_id_field)
    stations_list = Stations.objects.filter(fields_id_field=fields_id_field, station_active=1)
    print(stations_list)
    sensors = Sensors.objects.filter(sensor_active=1)
    return render(request, 'console/stations.html', {'stations_list':stations_list, 'sensors':sensors })

def sensors(request, idstation):
    #station = search_object_or_404(Sensors, stations_id_station=idstation)
    station = Sensors.objects.filter(stations_id_station=idstation, sensor_active=1)
    return render(request, 'console/sensors.html', {'station':station})

#class StationView(generic.DetailView):
#    model = Stations
#    template_name = 'console/station.html'
