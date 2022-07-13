from django.urls import path
from . import views

app_name="console"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/stations', views.StationsView.as_view(), name='stations'),
    path('<int:fields_id_field>/stations', views.stations, name = 'stations'),
    path('<int:pk>/station', views.StationView.as_view(), name='station'),

    #path('<int:pk>/fields/', views.FieldsView.as_view(), name='fields'),
]
