from django.urls import path

from user.views import  LoginView, UserProfile, Userview, Userdetailsview, RagisterView

urlpatterns = [
    path('users', Userview.as_view()),
    path('userdetails', Userdetailsview.as_view()),
    path('login', LoginView.as_view()),
    path('profile/<uuid:id>', UserProfile.as_view()),
    path('ragister', RagisterView.as_view())
]
