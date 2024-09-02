from rest_framework import serializers
from api.models import Podcast, Guest, Blog

#serializer 
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'medium_link']
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields="__all__"

class PodcastSerializer(serializers.ModelSerializer):
    guest_name = serializers.CharField(source='guest.name', read_only=True)
    blogs = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Podcast
        fields = ['id', 'series', 'title', 'release_date', 'guest_name', 'description', 'spotify_link', 'youtube_link', 'thumbnail','blogs']
