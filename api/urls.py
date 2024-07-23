from django.urls import path, include
from . import views
from rest_framework import routers, viewsets
from api.views import *

router=routers.DefaultRouter()
router.register(r'podcasts', PodcastViewSet)
router.register(r'guests', GuestViewSet)

urlpatterns = [
    path('', views.home, name='onrec-home'),
    path('api/', include(router.urls)),
    path('about/', views.about, name='onrec-about'),
    path('api/home/', home, name="home")
]