from django.urls import path
from GW_Website import views

urlpatterns = [
    path('', views.home, name='GymWale-home'),
]