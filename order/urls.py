from django.urls import path
from order.views import OrderDetailsView, OrderView, RecommendedProductView

urlpatterns = [
    path('orders', OrderView.as_view()),
    path('orderdetails', OrderDetailsView.as_view()),
    path('recommend-product', RecommendedProductView.as_view())
]
