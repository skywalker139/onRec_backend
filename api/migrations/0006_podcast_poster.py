# Generated by Django 5.1.4 on 2024-12-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_guest_social_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='poster',
            field=models.ImageField(default='onrec logo.jpg', upload_to='static/api'),
        ),
    ]