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

def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(to='/')

def updateStudent(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(data=request.post, instance=student)
        if form.is_valid():
            form.save()
            return redirect(to='/')
    return render(request=request, template_name='fbvApp/update.html', context={'student':student})
