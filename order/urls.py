from django.urls import path
# from .views import OrdersAPI
from order.views import OrdersView, OrderProductView
# from .views import Orders, OrderProductView


urlpatterns = [
    path("orders/", OrdersView.as_view()),
    path("orders/<int:pk>/", OrdersView.as_view()),
    path("order-product/", OrderProductView.as_view()),
    path("order-product/<int:pk>/", OrderProductView.as_view())
]

