from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Note(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(null=True)

    def __str__(self):
        return self.title + ': ' + self.text
