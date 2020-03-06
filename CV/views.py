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


    if name == 'XIAN' or name == 'xian':
        all_details = Legends.objects.get(L_codeName = 'Agent007')
        all_Education = Education.objects.filter(L_id = all_details.L_id)
        all_WorkExperience = WorkExperience.objects.filter(L_id = all_details.L_id)
        all_Skills = Skills.objects.filter(L_id = all_details.L_id)
        all_Works = Works.objects.filter(L_id = all_details.L_id)

    elif name == 'NILOY' or name == 'niloy':
        print('NILOY')
    elif name == 'NAHID' or name == 'nahid':
        print('NILOY')
    elif name == 'SAGIR' or name == 'sagir':
        print('NILOY')
    else:
        return HttpResponse(status=404)
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