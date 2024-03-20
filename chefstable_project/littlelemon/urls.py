from django.urls import path

from littlelemon import views

urlpatterns = [
    path('lemon', views.show_home),
]
