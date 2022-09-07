from django.core.mail import send_mail
import random
from django.conf import settings


def send_otp(email):
    subject = 'your account verification email'
    otp = random.randint(9999, 10000)
    message = f'your otp is {otp}'
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, email_from, [email])

    