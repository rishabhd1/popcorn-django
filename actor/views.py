from django.shortcuts import render, get_object_or_404
from django.views.generic import (TemplateView, ListView)
from .models import Actor

class ActorList(ListView):
    template_name = 'actors/actors.html'
    context_object_name = 'actors'
    queryset = Actor.objects.all()