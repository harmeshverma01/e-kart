from cart.views import CartView

from django.urls import path

urlpatterns = [
    path('cart', CartView.as_view())
]
