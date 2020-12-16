from django.db import models
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    insert_date = models.DateTimeField(default=timezone.now)
    user_id = models.IntegerField()

    def __str__(self):
        return self.title


class Word(models.Model):
    word = models.CharField(max_length=50)
    trans = models.CharField(max_length=150)
    user_id = models.IntegerField()
    source_id = models.IntegerField()

    def __str__(self):
        return self.word


class WordSource(models.Model):
    source_from = models.CharField(max_length=100)
    user_id = models.IntegerField()

    def __str__(self):
        return self.source_from
