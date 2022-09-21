from django.urls import path

from .views import CategoryView, ProductView, Productlistview,  StoreView, RatingView, StoreRagisterView

urlpatterns = [
    path('products', ProductView.as_view()),
    path('category', CategoryView.as_view()),
    path('product-list', Productlistview.as_view()),
    path('store', StoreView.as_view()),
    path('Create_store', StoreRagisterView.as_view()),
    path('rating', RatingView.as_view()),
    
]
