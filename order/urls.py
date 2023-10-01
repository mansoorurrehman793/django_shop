from django.urls import path
# from .views import OrdersAPI
from order.views import OrdersView,CartView
# from .views import Orders, OrderProductView


urlpatterns = [
    path("orders/", OrdersView.as_view()),
    path("orders/<int:pk>/", OrdersView.as_view()),
    path("cart/", CartView.as_view()),
    path("cart/<int:pk>/", CartView.as_view())
]

