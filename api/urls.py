from django.urls import path, include
from . import views
from rest_framework import routers, viewsets
from api.views import *

router=routers.DefaultRouter()
router.register(r'podcasts', PodcastViewSet)
router.register(r'guests', GuestViewSet)

urlpatterns = [
    path('podcasts/all', views.home, name="home"),
    path('explore/<str:series>/', views.explore, name='explore'),
    path('podcast/<int:podcast_id>/', views.podcast, name='get_podcast_by_id')
    #path('api/', include(router.urls)),
]