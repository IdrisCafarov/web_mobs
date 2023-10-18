import random
import string

from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
import xml.etree.ElementTree as ET
# from app.core.payment.epoint import KapitalPayment
from account.models import *
from django.shortcuts import get_object_or_404



def code_slug_generator(size=12, chars=string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def create_slug_shortcode(size, model_):
    new_code = code_slug_generator(size=size)
    qs_exists = model_.objects.filter(slug=new_code).exists()
    return create_slug_shortcode(size, model_) if qs_exists else new_code
