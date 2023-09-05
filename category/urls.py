from django.urls import path
from .apiviews import CategoriesList,CategoriesDetail
from .apiviews import SubCategoriesList,SubCategoriesDetail




urlpatterns = [

    path("Categories/", CategoriesList.as_view(), name="categories_list"),
    path("Categories/<int:pk>/", CategoriesDetail.as_view(), name="categories_detail"),
    path("SubCategories/", SubCategoriesList.as_view(), name="sub_categories_list"),
    path("SubCategories/<int:pk>/", SubCategoriesDetail.as_view(), name="sub_categories_detail")
]

