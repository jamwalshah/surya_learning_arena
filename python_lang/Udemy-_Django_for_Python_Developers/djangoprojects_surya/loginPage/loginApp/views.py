from django.shortcuts import render
from . import forms

# Create your views here.
def loginPageView(request):
    """takes a request and processes the form for validation, etc.
    Args:
        request (_HttpRequest_): _an HttpRequest object that contains metadata about the request_
    """
    form_data = forms.LoginForm()
    if request.method == 'POST':
        form_request_post = forms.LoginForm(request.POST)
        if form_request_post.is_valid():
            print('loginForm is valid')
            print('username is', form_request_post.cleaned_data['username'])
            print('password is', form_request_post.cleaned_data['password'])
    return render(request=request, template_name='loginPage.html', context={'form':form_data})
