from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import viewsets, status
from api.models import Podcast, Guest
from api.serializers import PodcastSerializer, GuestSerializer

class PodcastViewSet(viewsets.ModelViewSet):
    queryset=Podcast.objects.all()
    serializer_class=PodcastSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

    
@api_view(['GET'])
def home(request):
    podcasts = Podcast.objects.order_by('-release_date')[:5]
    serializer1 = PodcastSerializer(podcasts, many=True, context={'request': request})
    
    guests = Guest.objects.order_by('-created_at')[:3]
    serializer2 = GuestSerializer(guests, many=True, context={'request': request})
    
    data = {
        "recent5podcasts":serializer1.data,
        "recent3guests":serializer2.data
    }

    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def explore(request, series_name):
    podcasts = Podcast.objects.filter(series=series_name)
    serializer = PodcastSerializer(podcasts, many=True)
    return Response(serializer.data)

def about(request):
    return HttpResponse('<h1>About Page</h1>')