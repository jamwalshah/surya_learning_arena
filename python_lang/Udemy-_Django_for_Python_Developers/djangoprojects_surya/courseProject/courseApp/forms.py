from django import forms
from courseApp.models import Course

class CourseForm(forms.ModelForm):
    """Form definition for Course."""

    class Meta:
        """Meta definition for Courseform."""
        model = Course
        fields = '__all__'
