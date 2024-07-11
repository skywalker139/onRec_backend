from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from api.models import Podcast, Guest
from api.serializers import PodcastSerializer, GuestSerializer
class PodcastViewSet(viewsets.ModelViewSet):
    queryset=Podcast.objects.all()
    serializer_class=PodcastSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

def home(request):
    #return render(request, 'api/home.html')
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')