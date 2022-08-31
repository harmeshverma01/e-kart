from django.urls import path

from store.views import CategoryView, ProductView

urlpatterns = [
    path('products', ProductView.as_view()),
    path('category', CategoryView.as_view())
]
