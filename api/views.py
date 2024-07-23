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

# @api_view(['GET'])
# def latest_podcasts(request):
#     podcasts = Podcast.objects.order_by('-date')[:5]  # Get latest 5 podcasts
#     serializer = PodcastSerializer(podcasts, many=True)  # Serialize data
#     return Response(serializer.data)

    
@api_view(['GET'])
def home(request):
    podcasts = Podcast.objects.order_by('-date')[:5]
    # podcast_list = list(podcasts.values())
    serializer = PodcastSerializer(podcasts, many=True, context={'request': request})
    data = {
        "top3tilesdata":serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


def about(request):
    return HttpResponse('<h1>About Page</h1>')