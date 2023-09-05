from django.urls import path
from .apiviews import ImagesList
from .apiviews import ImagesDetail




urlpatterns = [

    path("Images/", ImagesList.as_view(), name="images_list"),
    path("Images/<int:pk>/", ImagesDetail.as_view(), name="images_detail"),

]

