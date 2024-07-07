# Generated by Django 5.0.6 on 2024-07-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('podcast_series', models.CharField(choices=[('Startup Podcast', 'Startup Podcast'), ('Entrepreneurial Echoes by onRec', 'Entrepreneurial Echoes by onRec'), ('Class of 2020s', 'Class of 2020s'), ('Career podcast', 'Career podcast')], max_length=50)),
                ('podcast_title', models.CharField(max_length=50)),
                ('date_uploaded', models.DateField()),
                ('description', models.TextField()),
                ('spotify_link', models.URLField()),
                ('youtube_link', models.URLField()),
            ],
        ),
    ]