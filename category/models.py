from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default=None)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    categories = models.ForeignKey(
        Categories, related_name="categories", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
