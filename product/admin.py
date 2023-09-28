from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):

    # list_display = ['title', "product_sku", "price", "availability", "quantity", "create_date"]
    list_display = [field.name for field in Product._meta.fields]
    list_filter = [field.name for field in Product._meta.fields]
    # readonly_fields = ('price',)
    search_fields = ["title", "product_sku"]


# Register your models here.
# admin.site.register(Product)
