from django.urls import path
from . import views

urlpatterns = [
    #/
    path('', views.testingshits, name='Testing Shits'),
]