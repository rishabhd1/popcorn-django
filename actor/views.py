from django.shortcuts import render, get_object_or_404
from django.views.generic import (TemplateView, ListView, DetailView, CreateView)
from .models import Actor

class ActorList(ListView):
    template_name = 'actors/actors.html'
    context_object_name = 'actors'
    queryset = Actor.objects.all()

class ActorDetail(DetailView):
    template_name = 'actors/actors_detail.html'
    context_object_name = 'actors_detail'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Actor, id=id_)

class ActorCreate(CreateView):
    template_name = 'actors/create.html'
    context_object_name = 'actors_create'
