from django.contrib import admin
from .models import Images



@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Images._meta.fields]
    list_filter = [field.name for field in Images._meta.fields]

    search_fields = ["title", "image", "product_id"]
    
