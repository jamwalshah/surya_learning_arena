from django.shortcuts import render
from modelForms.forms import ProjectForm
from modelForms.models import Project

# Create your views here.
def index(request):
    return render(request=request, template_name='modelForms/index.html')

def listProjects(request):
    projectsList = Project.objects.all()
    return render(request=request, template_name='modelForms/listProjects.html', context={'projects':projectsList})

def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request=request)
    return render(request=request, template_name='modelForms/AddProject.html', context={'form':form})
