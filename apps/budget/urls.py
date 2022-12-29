from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.InputView.as_view(), name='budget-home'),
    path('month/', views.MonthDetail.as_view(), name='budget-month'),
    path('month/<str:year_month>', views.MonthDetail.as_view(), name='budget-month-detail'),
    path('item/<int:pk>', views.EditItemView.as_view(), name='edit-item'),
    path('chart/', views.ChartView.as_view(), name='budget-chart'),
]
