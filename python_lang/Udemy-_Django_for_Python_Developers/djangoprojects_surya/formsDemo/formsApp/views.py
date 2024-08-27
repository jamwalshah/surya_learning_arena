from django.shortcuts import render
from . import forms

# Create your views here.
def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST) # form object will have all the data that user submits
        if form.is_valid():
            print("Form is valid")
            print("First Name", form.cleaned_data['firstName'])
            print("Last Name", form.cleaned_data['lastName'])
            print("Email", form.cleaned_data['email'])
            # print("form:", form) # debug
            # print("form.cleaned_data:", form.cleaned_data) # debug
    return render(request=request, template_name='formsDemo/userRegistration.html', context={'form':form})
