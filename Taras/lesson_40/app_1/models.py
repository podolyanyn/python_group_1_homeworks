from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    reminder = models.DateTimeField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
