from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Notes(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    reminder = models.DateTimeField("reminder")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.text}, {self.reminder}, {self.category}'



