from django.db import models
from django.utils import timezone



choices=(('Startup Podcast','Startup Podcast'),('Entrepreneurial Echoes by onRec','Entrepreneurial Echoes by onRec'), 
         ('Class of 2020s','Class of 2020s'),('Career podcast','Career podcast'))

# Models
class Guest(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.TextField()
    designation=models.TextField()
    image=models.ImageField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Podcast(models.Model):
    id=models.AutoField(primary_key=True)
    series=models.CharField(max_length=50, choices=choices)
    title=models.CharField(max_length=50)
    release_date=models.DateField(default=timezone.now)
    guest=models.ForeignKey(Guest, on_delete=models.CASCADE)
    description=models.TextField()
    spotify_link=models.URLField()
    youtube_link=models.URLField()
    thumbnail=models.ImageField(default='onrec logo.jpg' ,upload_to='static/api')

    def __str__(self):
        return self.title
        