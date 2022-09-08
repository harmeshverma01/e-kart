from django.urls import path

from user.views import ( 
    CreateprofileView, 
    ForgetPasswordView, 
    LoginView,
    ResetpasswordView, 
    UserProfile, 
    Userview, 
    Userdetailsview, 
    RagisterView, 
    ValidatedOtp
)


urlpatterns = [
    path('users', Userview.as_view()),
    path('userdetails', Userdetailsview.as_view()),
    path('login', LoginView.as_view()),
    path('profile', UserProfile.as_view()),
    path('register', RagisterView.as_view()),
    path('create-profile', CreateprofileView.as_view()),
    path('forget-password', ForgetPasswordView.as_view()),
    path('validate-otp', ValidatedOtp.as_view()),
    path('reset_password', ResetpasswordView.as_view())
]
