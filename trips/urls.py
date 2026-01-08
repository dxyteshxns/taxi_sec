from django.urls import path

from . import views

app_name = 'trips'

urlpatterns = [
    path('', views.TripListView.as_view(), name='trip_list'),
    path('create/', views.TripCreateView.as_view(), name='trip_create'),
    path('<int:pk>/', views.TripDetailView.as_view(), name='trip_detail'),
    path('<int:pk>/update/', views.TripUpdateView.as_view(), name='trip_update'),
    path('<int:pk>/delete/', views.TripDeleteView.as_view(), name='trip_delete'),
    path('available/', views.AvailableTripsView.as_view(), name='available_trips'),
    path('<int:pk>/accept/', views.accept_trip, name='accept_trip'),
    path('<int:pk>/complete/', views.complete_trip, name='complete_trip'),
    path('<int:pk>/cancel/', views.cancel_trip, name='cancel_trip'),
]
