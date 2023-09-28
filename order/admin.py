from django.contrib import admin
from .models import Orders, OrderProduct

# Register your models here.
# admin.site.register(Orders)
# admin.site.register(OrderProduct)



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):

    # list_display = ['title', "product_sku", "price", "availability", "quantity", "create_date"]
    list_display = [field.name for field in OrderProduct._meta.fields]
    list_filter = [field.name for field in OrderProduct._meta.fields]
    # readonly_fields = ('price',)