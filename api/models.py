from django.db import models

# Create your models here.
class Guest(models.Model):
    guest_name=models.CharField(primary_key=True, max_length=50)
    guest_description=models.TextField()

class Podcast_post(models.Model):
    id=models.AutoField(primary_key=True)
    podcast_series=models.CharField(max_length=20)
    podcast_title=models.CharField(max_length=50)
    date_uploaded=models.DateField(auto_now=False, auto_now_add=False)
    guest=models.ForeignKey(Guest)
    description=models.TextField()
    spotify_link=models.URLField()
    youtube_link=models.URLField()
    thumbnail=models.ImageField()