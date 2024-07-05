from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict={"name":"Surya"}
    return render(request=request, template_name='templatesApp/firstTemplate.html', context=myDict)

def renderEmployee(request):
    myDict={"id":123, "name":"Johnny", "sal":10000}
    return render(request=request, template_name='templatesApp/employeeTemplate.html', context=myDict)