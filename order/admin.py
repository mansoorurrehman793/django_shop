from django.contrib import admin
from .models import Orders, Cart

# Register your models here.
# admin.site.register(Orders)
# admin.site.register(OrderProduct)



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    # list_display = ['title', "product_sku", "price", "availability", "quantity", "create_date"]
    list_display = [field.name for field in Cart._meta.fields]
    list_filter = [field.name for field in Cart._meta.fields]
    # readonly_fields = ('price',)