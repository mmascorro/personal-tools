from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.site_login, name='login'),
    path('logout/', views.site_logout, name='logout'),
]