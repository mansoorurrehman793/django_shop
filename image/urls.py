from django.urls import path
# from .apiviews import ImagesList
# from .apiviews import ImagesDetail

from .views import ImageAPI




urlpatterns = [
    path("Images/", ImageAPI.as_view()),
    path("Images/<int:pk>/", ImageAPI.as_view()),
    # path("Images/", ImageAPI.as_view()),
    # path("Images/<int:pk>/", ImageAPI.as_view())
]
