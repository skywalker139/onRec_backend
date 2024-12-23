from django.db import models
from django.utils import timezone



choices=(('startup','startup'),('Entrepreneurial','Entrepreneurial'), 
         ('Classof','Classof'),('career','career'),('offbeat','offbeat'),('wellness','wellness'))


def validate_json_content(value):
    if not isinstance(value, list):
        raise ValidationError("Content must be a list of dictionaries.")
    for item in value:
        if not isinstance(item, dict) or 'heading' not in item or 'paragraph' not in item:
            raise ValidationError("Each item in the content list must be a dictionary with 'heading' and 'paragraph' keys.")


# Models
class Guest(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.TextField()
    designation=models.TextField()
    image=models.ImageField()
    created_at = models.DateTimeField(default=timezone.now)
    social_link = models.URLField(default='https://www.instagram.com/iitr_onrec/')

    def __str__(self):
        return self.name

class Podcast(models.Model):
    id=models.AutoField(primary_key=True)
    series=models.CharField(max_length=50, choices=choices)
    title=models.CharField(max_length=100)
    release_date=models.DateField(default=timezone.now)
    guest=models.ForeignKey(Guest, on_delete=models.CASCADE)
    description=models.TextField()
    spotify_link=models.URLField()
    youtube_link=models.URLField()
    thumbnail=models.ImageField(default='onrec logo.jpg' ,upload_to='static/api')
    poster=models.ImageField(default='onrec logo.jpg' ,upload_to='static/api')

    def __str__(self):
        return self.title
        
class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content = models.JSONField(
        default=list,
        validators=[validate_json_content],
        help_text="Enter JSON data as a list of dictionaries with 'heading' and 'paragraph' keys."
    )
    release_date=models.DateField(default=timezone.now)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='blogs')
    medium_link=models.URLField()

    def __str__(self):
        return self.title