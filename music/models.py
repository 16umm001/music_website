# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=400)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title + '_ ' + self.artist
class song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)