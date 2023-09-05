from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    #  Category has_many SubCatagories 
    # Category has_many Products

    def __str__(self):
        return self.name
    

class SubCategories(models.Model):
    id = models.AutoField(primary_key=True)
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)


    def __str__(self):
        return self.name
    # SubCatagory has_many Images



# class Images(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     url = models.CharField(max_length=255)

