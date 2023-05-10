from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField


class Music(models.Model):
    user = models.ForeignKey(User, related_name='song_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False, blank=False)
    artist = models.CharField(max_length=500, null=False, blank=False)
    album = models.ForeignKey(
        'Album', on_delete=models.SET_NULL, null=True, blank=True)
    time_length = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True)
    audio_file = models.FileField(
        upload_to='musics')
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='music_image/', force_format='WEBP',
        blank=False, null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)

    class meta: 
        ordering = ['-posted_date']

        def __str__(self):
            return str(self.title)

    def save(self, *args, **kwargs):
        if not self.time_length:

            pass
        return super().save(*args, **kwargs)


class album(models.Model):
    name = models.CharField(max_length=500)