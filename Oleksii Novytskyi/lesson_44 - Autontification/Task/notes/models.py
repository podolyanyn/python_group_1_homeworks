from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Notes(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField('reminder date')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.categories}, {self.title}, {self.text}, {self.reminder}"
