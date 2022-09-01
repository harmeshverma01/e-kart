from django.urls import path

from user.views import  CreateprofileView, LoginView, UserProfile, Userview, Userdetailsview, RagisterView

urlpatterns = [
    path('users', Userview.as_view()),
    path('userdetails', Userdetailsview.as_view()),
    path('login', LoginView.as_view()),
    path('profile', UserProfile.as_view()),
    path('register', RagisterView.as_view()),
    path('create-profile', CreateprofileView.as_view())
]
