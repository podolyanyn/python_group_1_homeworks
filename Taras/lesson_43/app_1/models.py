from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=50)
