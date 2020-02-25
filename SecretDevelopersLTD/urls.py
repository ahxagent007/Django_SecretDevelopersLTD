from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('skills/', include('skills.urls')),
    path('CV/', include('CV.urls'))

]
