from django.shortcuts import render
from . import forms

# Create your views here.
def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    return render(request=request, template_name='formsDemo/userRegistration.html', context={'form':form})
