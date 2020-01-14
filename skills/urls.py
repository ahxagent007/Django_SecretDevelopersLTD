from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.allList, name='allList'),

]