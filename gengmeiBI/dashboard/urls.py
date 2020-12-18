from django.contrib import admin
from django.urls import path, re_path
from dashboard import views # 从自己的 app 目录引入 views
urlpatterns = [
    path('index/', views.index),
    ]