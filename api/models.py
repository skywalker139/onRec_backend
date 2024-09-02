from django.db import models
from django.utils import timezone



choices=(('startup','startup'),('Entrepreneurial','Entrepreneurial'), 
         ('Classof','Classof'),('career','career'),('offbeat','offbeat'),('wellness','wellness'))

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
        
class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    release_date=models.DateField(default=timezone.now)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='blogs')
    medium_link=models.URLField()

    def __str__(self):
        return self.title