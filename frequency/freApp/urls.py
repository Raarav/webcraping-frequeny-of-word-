from django.urls import path
from . import views

urlpatterns=[
    path('', views.frequency),
    path('result', views.results),
]