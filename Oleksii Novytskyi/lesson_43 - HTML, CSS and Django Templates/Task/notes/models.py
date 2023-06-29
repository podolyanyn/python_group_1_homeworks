from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Notes(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField('reminder date')

    def __str__(self):
        return f"{self.categories}, {self.title}, {self.text}, {self.reminder}"
