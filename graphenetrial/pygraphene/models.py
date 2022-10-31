from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=100)
    genre = models.TextField()
    category = models.ForeignKey(
        Category, related_name="movies", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name