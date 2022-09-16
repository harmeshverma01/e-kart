from django.core.mail import send_mail
from django.conf import settings

from rest_framework.pagination import PageNumberPagination



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
    
class StandardResultSetPage(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page'
    max_page_size = 10