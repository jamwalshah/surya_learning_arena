from django.shortcuts import render, redirect
from fbvApp.models import Student
from fbvApp.forms import StudentForm

# Create your views here.
def getStudents(request):
    students = Student.objects.all()
    return render(request=request, template_name='fbvApp/index.html', context={'students':students})

def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(to='/')
    return render(request=request, template_name='fbvApp/create.html', context={'form':form})
