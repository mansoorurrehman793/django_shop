from django.urls import path
from .views import CategoryAPI, SubCategoryAPI




urlpatterns = [
    path("categories/", CategoryAPI.as_view(), name="categories_list"),
    path("categories/<int:pk>/", CategoryAPI.as_view(), name="categories_detail"),
    path("sub-categories/", SubCategoryAPI.as_view(), name="sub_categories_list"),
    path("sub-categories/<int:pk>/", SubCategoryAPI.as_view(), name="sub_categories_detail")
]

