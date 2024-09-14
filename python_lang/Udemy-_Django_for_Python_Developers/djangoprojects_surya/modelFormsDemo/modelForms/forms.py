from django import forms
from modelForms.models import Project

class ProjectForm(forms.ModelForm):
    """Form definition for Project."""

    class Meta:
        """Meta definition for Projectform."""

        model = Project
        fields = '__all__'
        