from django.urls import path, include
from actor.views import ActorList, ActorDetail

urlpatterns = [
    path('', ActorList.as_view(), name='actors'),
    path('<int:id>/', ActorDetail.as_view(), name='actor_detail')
]
