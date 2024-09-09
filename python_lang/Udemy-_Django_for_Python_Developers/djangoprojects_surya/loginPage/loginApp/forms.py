from django import forms
from django.core import validators
import re

def clean_password(self):
    inputPassword = self.cleaned_data["password"]
    if not re.search(pattern=r'[A-Z]', string=inputPassword):
        raise forms.ValidationError(message='Password must contain at-least one uppercase letter')
    # if len(inputPassword)<8:
    #     raise forms.ValidationError(message='Password should be at-least 8 characters long')
    return inputPassword

class LoginForm(forms.Form):
    """
    LoginForm:
        - has two fields userName and password with a Submit button
        - Inherits the properties from `django.forms.Form`
    """
    username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        # validators=[
        #     validators.RegexValidator(
        #         regex=r'^(?=.+[A-Z])[^\s]+$',
        #         message='Password must contain at-least one uppercase letter')]
        )


    
