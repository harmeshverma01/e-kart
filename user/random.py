from django.core.mail import send_mail
from django.conf import settings
import random

def send_otp(email, otp):
    subject = 'your account verification email'
    message = f'your otp is {otp} '
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject,
        message,
        email_from,
        [email],
        fail_silently = False
    )
    
    
