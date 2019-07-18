from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Actor
from .forms import ActorModelForm
from django.urls import reverse


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
    queryset = Actor.objects.all()
    form_class = ActorModelForm


class ActorUpdate(UpdateView):
    template_name = 'actors/create.html'
    queryset = Actor.objects.all()
    form_class = ActorModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Actor, id=id_)


class ActorDelete(DeleteView):
    template_name = 'actors/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Actor, id=id_)

    def get_success_url(self):
        return reverse('actors')
