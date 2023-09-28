from django.urls import path
from product.views import ProductView


urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<int:pk>/", ProductView.as_view())
]
