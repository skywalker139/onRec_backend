from rest_framework import serializers
from api.models import Podcast

#serializer 
class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Podcast
        fields="__all__"