from django.db import models


choices=(('Startup Podcast','Startup Podcast'),('Entrepreneurial Echoes by onRec','Entrepreneurial Echoes by onRec'), 
         ('Class of 2020s','Class of 2020s'),('Career podcast','Career podcast'))

# Models
class Guest(models.Model):
    name=models.CharField(primary_key=True, max_length=50)
    description=models.TextField()
    designation=models.TextField(max_length=20)
    image=models.ImageField()

    def __str__(self):
        return self.name

class Podcast(models.Model):
    id=models.AutoField(primary_key=True)
    series=models.CharField(max_length=50, choices=choices)
    title=models.CharField(max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=False)
    name=models.ForeignKey(Guest, on_delete=models.CASCADE)
    description=models.TextField()
    spotify_link=models.URLField()
    youtube_link=models.URLField()
    thumbnail=models.ImageField(default='onrec logo.jpg' ,upload_to='static/api')

    def __str__(self):
        return self.title
        