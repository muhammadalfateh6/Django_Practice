from django.urls import path
from demoapp1 import views

urlpatterns = [
    path('home_1/', views.home_1),
    path('menu_1/', views.menu_1),
    path('about_1/', views.about_1),
    path('CustomerInfo/', views.get_cm_info),
    path('about/', views.about_littlelemon),
    path('greet/', views.index),
    path('menu/', views.menu),
    path('menu_id/', views.menu_byid),
    path('check/', views.check),
    # path('demoform', views.form_view),
]