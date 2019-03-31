from django.views.generic import TemplateView

class ActorView(TemplateView):
    template_name = "actors/actors.html"
