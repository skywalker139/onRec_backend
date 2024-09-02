from import_export import resources 
from .models import Podcast, Guest, Blog
class PodcastResource(resources.ModelResource):
     class Meta:
         model = Podcast

class GuestResource(resources.ModelResource):
     class Meta:
         model = Guest

class BlogResource(resources.ModelResource):
     class Meta:
         model = Blog