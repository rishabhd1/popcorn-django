from django.urls import path, include
from actor.views import ActorList

urlpatterns = [
    path('', ActorList.as_view(), name='actors'),
]
