from django.db import models
from django.contrib.auth.models import User


class Music(models.Model):
    user = models.ForeignKey(
        User, related_name='song_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False, blank=False)
    artist = models.CharField(max_length=500, null=False, blank=False)
    audio_file = models.FileField(
        upload_to='musics/', default='')
    time_length = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.title)
