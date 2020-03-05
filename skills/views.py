from django.http import HttpResponse
from .models import Skills
from django.template import loader

def index(request):
    all_skills = Skills.objects.all()
    template = loader.get_template('skills/skills.html')
    #H:/07. Secret Developers LTD (Website)/SecretDevelopersLTD/SecretDevelopersLTD/templates/skills
    context = {
        'all_skills': all_skills
    }

    return HttpResponse(template.render(context, request))

def allList(request):
    return HttpResponse("<h1>SKILLS HOME ALL LIST HERE</h1>")

def singleSkill(request, skill_id):
    return HttpResponse("<h1>SKILLS id is "+str(skill_id)+"</h1>")