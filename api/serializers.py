from rest_framework import serializers
from api.models import Podcast, Guest

#serializer 
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields="__all__"

class PodcastSerializer(serializers.ModelSerializer):
    guest_name = serializers.CharField(source='guest.name', read_only=True)

    class Meta:
        model = Podcast
        fields = ['id', 'series', 'title', 'release_date', 'guest_name', 'description', 'spotify_link', 'youtube_link', 'thumbnail']
