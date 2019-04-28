from django.urls import path, include
from actor.views import ActorList, ActorDetail, ActorCreate

urlpatterns = [
    path('', ActorList.as_view(), name='actors'),
    path('create/', ActorCreate.as_view(), name='actor_create'),
    path('<int:id>/', ActorDetail.as_view(), name='actor_detail'),
    # path('<int:id>/update/', ActorDetail.as_view(), name='actor_detail'),
    # path('<int:id>/delete/', ActorDetail.as_view(), name='actor_detail')
]
