from django import forms
from .models import Actor


class ActorModelForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = [
            'name',
            'sex',
            'dateOfBirth',
            'bio',
            'image'
        ]
