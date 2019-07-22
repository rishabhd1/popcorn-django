from django import forms
from .models import Movie


class MoiveModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'producer',
            'name',
            'yearOfRelease',
            'plot',
            'plot',
            'actors',
        ]
