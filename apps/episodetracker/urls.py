from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='episodetracker-home'),
    path('shows/', views.ShowView.as_view()),
    path('shows/<int:id>', views.ShowUpdateView.as_view()),
]
