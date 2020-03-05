from django.contrib import admin
from .models import Legends, WorkExperience, Education, Skills

# Register your models here.

admin.site.register(Legends)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Skills)