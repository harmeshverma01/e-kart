from django.urls import path
from order.views import OrderDetailsView, OrderView

urlpatterns = [
    path('orders', OrderView.as_view()),
    path('orderdetails', OrderDetailsView.as_view())
]
