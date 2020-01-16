from django.urls import path
from . import views

urlpatterns = [
    #/skills/
    path('', views.index, name='index'),
    #/skills/list/
    path('list', views.allList, name='allList'),
    #/skills/1111
    path('<int:skill_id>', views.singleSkill, name='singleSkill'),

]