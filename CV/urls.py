from django.urls import path
from . import views

urlpatterns = [
    #/
    path('', views.CV, name='CV'),
    path('<name>', views.CVshow, name='CV-Show')
]