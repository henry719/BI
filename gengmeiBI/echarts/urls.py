from django.urls import path
from echarts import views

urlpatterns = [
    path('index/', views.index),
    ]
