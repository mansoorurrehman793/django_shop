from django.db import models
from django.contrib.auth.models import User
from category.models import Categories, SubCategories

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    sub_categoery = models.ForeignKey(
        SubCategories, on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=255)
    description = models.TextField()
    details = models.TextField()
    price = models.FloatField(default=0, blank=True)
    availability = models.IntegerField(default=0, blank=True)
    quantity = models.IntegerField(default=0, blank=True)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
