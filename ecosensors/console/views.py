from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Fields, Stations


class IndexView(generic.ListView):
    template_name = 'console/index.html'
    context_object_name = 'fields_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Fields.objects.order_by('-field_created')[:5]


class FieldsView(generic.DetailView):
    model = Fields
    template_name = 'console/fields.html'


class StationsView(generic.ListView):
    #model = Stations
    context_object_name = 'stations_list'
    template_name = 'console/stations.html'

    def get_queryset(self):
        """Return the last five published station."""
        return Stations.objects.order_by('-station_created')[:10]

def stations(request, fields_id_field):
    #template = loader.get_template('console/stations.html')
    #try:
    stations_list = get_object_or_404(Stations, pk=fields_id_field)
    #except(KeyError, Stations.DoesNotExist):
    #    return render(request, 'console/stations.html', {'stations_list': '1'})
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % fields_id_field)

    #try:
    return render(request, 'console/stations.html', {'stations_list':stations_list})
    #except(KeyError, Stations.DoesNotExist):
    #    return render(request, 'console/stations.html', {'stations_list':'1'})

class StationView(generic.ListView):
    model = Stations
    template_name = 'console/stations.html'
