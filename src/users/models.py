# Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from datetime import datetime
import os
# Create your models here.


@python_2_unicode_compatible
class Videos(models.Model):

    def __str__(self):
        return 'User: ' + self.user.username + ' Name: ' + self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def filename(self):
        return os.path.basename(self.video.name)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Video itself
    video = models.FileField(upload_to='static')
    # Data about the video.
    name = models.CharField(max_length=100, default="test")
    pub_date = models.DateTimeField('date published', default=datetime.now())
    description = models.CharField(max_length=250)
    # Controlling how many views has a video.
    views = models.IntegerField(default=0)
    # Controlling the upvotes of a video.
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    tags = models.TextField(default='video')
    private= models.BooleanField(default=False)
