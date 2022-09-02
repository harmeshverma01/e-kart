from cart.views import CartView

from django.urls import path

urlpatterns = [
    path('cart/<uuid:id>', CartView.as_view())
]
