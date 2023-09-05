from django.urls import path
from .apiviews import ProductList,ProductDetail
# from .apiviews import CategoriesList,CategoriesDetail
# from .apiviews import ImagesList,ImagesDetail



urlpatterns = [
    path("Product/", ProductList.as_view(), name="product_list"),
    path("Product/<int:pk>/", ProductDetail.as_view(), name="product_detail"),

    # path("Categories/", CategoriesList.as_view(), name="categories_list"),
    # path("Categories/<int:pk>/", CategoriesDetail.as_view(), name="categories_detail"),

    # path("Images/", ImagesList.as_view(), name="image_list"),
    # path("Images/<int:pk>/", ImagesDetail.as_view(), name="image_detail")
]


    
    
    #  path("vote/", CreateVote.as_view(), name="create_vote"),
