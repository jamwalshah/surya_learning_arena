from django import forms
from movieApp.models import Movie

class MovieForm(forms.ModelForm):
    """Form definition for Movie."""

    class Meta:
        """Meta definition for Movieform."""

        model = Movie
        fields = '__all__'
