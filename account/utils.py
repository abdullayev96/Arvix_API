import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .models import *


#
#
# def generate_otp(length=6):
#     characters = string.digits
#     otp = ''.join(random.choice(characters) for _ in range(length))
#     return otp
#
#
#
# def send_otp_email(email, otp):
#     subject = 'Your OTP for Login'
#     message = f'Your OTP is: {otp}'
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message, from_email, recipient_list)
#


def send_otp_email(email):
    subject = 'Your account verification email is'
    otp  = random.randint(10000, 99999)
    from_email = settings.EMAIL_HOST
    message = f'This is Your  OTP {otp}'


    send_mail(subject, message, from_email, [email])
    user_obj = CustomUser.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()



def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp


