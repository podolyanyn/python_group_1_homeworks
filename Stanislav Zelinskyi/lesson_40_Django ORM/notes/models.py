from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, default='default')

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
