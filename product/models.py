from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=255)
    description = models.TextField(default=None)
    details = models.TextField(default=None)
    price = models.FloatField(default=0)
    availability = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    #  Products has_many images
    # Product belongs_to Catagory through category_id
    # Product belongs_to Subcategory through subcategory_id
    def __str__(self):
        return self.title

