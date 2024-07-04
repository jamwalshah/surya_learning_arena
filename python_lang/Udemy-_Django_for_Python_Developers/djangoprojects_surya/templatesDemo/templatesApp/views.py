from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict={"name":"Surya"}
    return render(request=request, template_name='templatesApp/firstTemplate.html', context=myDict)