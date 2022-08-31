from django.urls import path

from .views import CategoryView, ProductView, Productlistview, StoreView

urlpatterns = [
    path('products', ProductView.as_view()),
    path('category', CategoryView.as_view()),
    path('product-list', Productlistview.as_view()),
    path('store', StoreView.as_view())
]
