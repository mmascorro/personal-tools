from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='mileage-home'),
    path('create/', views.CreateTripView.as_view(), name='trip-create'),
    path('trip/<int:pk>/', views.TripDetailView.as_view(), name='trip-detail'),
    path('leg/<int:pk>/', views.LegEditView.as_view(), name='leg-edit'),
]
