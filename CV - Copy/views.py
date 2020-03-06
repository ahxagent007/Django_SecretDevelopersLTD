from tempfile import template
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from CV.models import Legends, WorkExperience, Skills, Education, Works

def CV(request):

    data = {
        'title': 'CV'
    }

    print(type(data))


    template = loader.get_template('CV/CV.html')

    return HttpResponse(template.render(data, request))

def CVshow(request, name):


    if name == 'XIAN' or name == 'xian' or name == 'Xian':
        all_details = Legends.objects.get(L_codeName = 'Agent007')

    elif name == 'NILOY' or name == 'niloy' or name == 'Niloy':
        all_details = Legends.objects.get(L_codeName = 'Niloy')

    elif name == 'NAHID' or name == 'nahid' or name == 'Nahid':
        all_details = Legends.objects.get(L_codeName = 'Nahid')

    elif name == 'SAGIR' or name == 'sagir' or name == 'Sagir':
        all_details = Legends.objects.get(L_codeName = 'Sagir')

    else:
        return HttpResponse(status=404)

    all_Education = Education.objects.filter(L_id=all_details.L_id)
    all_WorkExperience = WorkExperience.objects.filter(L_id=all_details.L_id)
    all_Skills = Skills.objects.filter(L_id=all_details.L_id)
    all_Works = Works.objects.filter(L_id=all_details.L_id)

    data = {
        'title': name,
        'legend': all_details,
        'E': all_Education,
        'WE': all_WorkExperience,
        'S': all_Skills,
        'W' : all_Works
    }

    template = loader.get_template('CV/CV.html')

    return HttpResponse(template.render(data, request))