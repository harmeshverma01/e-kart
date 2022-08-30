from django.urls import path

from user.views import  LoginView, UserProfile, Userview, Userdetailsview

urlpatterns = [
    path('users', Userview.as_view()),
    path('userdetals/<uuid:id>', Userdetailsview.as_view()),
    path('login', LoginView.as_view()),
    path('profile', UserProfile.as_view())
]
