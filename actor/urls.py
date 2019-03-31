from django.urls import path, include
from actor.views import ActorView

urlpatterns = [
    path('', ActorView.as_view(), name='actors'),
]
