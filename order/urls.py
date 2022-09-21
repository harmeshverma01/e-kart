from django.urls import path
from order.views import Applycoupencode, OrderDetailsView, OrderView, RecommendedProductView, CreatecoupenView

urlpatterns = [
    path('orders', OrderView.as_view()),
    path('orderdetails', OrderDetailsView.as_view()),
    path('recommend-product', RecommendedProductView.as_view()),
    path('create_coupen', CreatecoupenView.as_view()),
    path('apply_coupen', Applycoupencode.as_view()),
]
