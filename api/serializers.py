from rest_framework import serializers
from api.models import Podcast, Guest

#serializer 
class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    podcast_id=serializers.ReadOnlyField()
    class Meta:
        model=Podcast
        fields="__all__"

class GuestSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Guest
        fields="__all__"