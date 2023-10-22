from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,on_delete=models.SET_NULL, null=True, related_name="cart_items"
    )
    product =  models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)

    is_exclude = models.BooleanField(default=False, db_comment="to check the item that need to be exclude from the cart",)

    # flag_reason = models.CharField(max_length=255, blank=True, null=True)

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # available_quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, default="", blank=True)
    total_price = models.FloatField(blank=True, default=0.0)
    order_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Order {self.order_number} by {self.user.username}"
    

