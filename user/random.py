import math, random
from django.core.mail import EmailMessage

from user.serializer import ForgetpasswordSerializer


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() *10)]
    return OTP


def send_mail(request):
    email = EmailMessage(
        'Title',
        (ForgetpasswordSerializer.otp),
        'my-email',
        ['my-receive-email']
    )
    email.attach_file(ForgetpasswordSerializer.file)
    email.send()
    