from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class CartItem(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product)
    # quantity = models.PositiveIntegerField(default=1)
    cart_items = models.ManyToManyField(CartItem)

    def __str__(self):
        return f"{self.user.username}"

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
    

# class OrderProduct(models.Model):
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     class Meta:
#         unique_together = ('user', 'product')


#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} in  {self.user.username}"