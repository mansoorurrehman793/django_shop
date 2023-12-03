from django.db import models
from product.models import Product

# Create your models here.Product

class Images(models.Model):
    id = models.AutoField( primary_key=True)
    product_id = models.ForeignKey(Product, related_name='Images',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
