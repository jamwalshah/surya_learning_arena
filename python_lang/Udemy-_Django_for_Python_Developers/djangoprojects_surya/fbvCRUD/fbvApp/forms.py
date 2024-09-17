from fbvApp.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    """Form definition for Student."""

    class Meta:
        """Meta definition for Studentform."""
        model = Student
        fields = '__all__'
        
