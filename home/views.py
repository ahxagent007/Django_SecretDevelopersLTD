from django.template import loader

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #all_skills = Skills.objects.all()
    template = loader.get_template('home/home.html')
    # H:/07. Secret Developers LTD (Website)/SecretDevelopersLTD/SecretDevelopersLTD/templates/skills
    context = {
        'info': 'HOME+'
    }

    return HttpResponse(template.render(context, request))