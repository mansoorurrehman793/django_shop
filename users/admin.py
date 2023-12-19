from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Register your models here.
# @admin.register(User,UserModelAdmin)
class UserAdmin(admin.ModelAdmin):
    pass

class UserModelAdmin(BaseUserAdmin):
   pass

    # list_filter = ["is_active", "is_staff", "is_superuser"]
    # fieldsets = (
    #     (None, {"fields": ("email", "password")}),
    #     ("Personal info", {"fields": ("username",)}),
    #     ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    # )
   

# Register the User model with the UserModelAdmin

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_display = ["id","email", "name", "tc", "is_admin"]
    # list_filter = ["is_admin"]
    # fieldsets = [
    #     ("User Credentials", {"fields": ["email", "password"]}),
    #     ("Personal info", {"fields": ["name","tc"]}),
    #     ("Permissions", {"fields": ["is_admin"]}),
    # ]


admin.site.register(User, UserModelAdmin)


