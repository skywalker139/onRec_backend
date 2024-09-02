from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import viewsets, status
from api.models import Podcast, Guest, Blog
from api.serializers import PodcastSerializer, GuestSerializer, BlogSerializer

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
def explore(request, series):
    if series == 'all':
        podcasts = Podcast.objects.all()
    else:
        podcasts = Podcast.objects.filter(series=series)

    serializer3 = PodcastSerializer(podcasts, many=True, context={'request': request})
    return Response(serializer3.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def podcast(request, podcast_id):
    try:
        podcast = Podcast.objects.get(id=podcast_id)
        guest=podcast.guest
        serializer1 = PodcastSerializer(podcast, context={'request': request})
        serializer2 = GuestSerializer(guest, context={'request': request})

        blog = Blog.objects.filter(podcast=podcast).first()
        blog_data = BlogSerializer(blog, context={'request': request})

        data = {
        "podcast":serializer1.data,
        "associatedguest":serializer2.data,
        "blog": blog_data.data
        }

        return Response(data, status=status.HTTP_200_OK)
    except Podcast.DoesNotExist:
        return Response({"error": "Podcast not found"}, status=status.HTTP_404_NOT_FOUND)
