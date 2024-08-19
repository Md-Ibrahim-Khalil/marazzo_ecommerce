from django.contrib.auth.models import User
from django.db import models
import re 
from django.core.validators import RegexValidator

PHONE_REGEX = RegexValidator(
    regex=r"^01[13-9]\d{8}$",
    message="Phone number must be 11 digit & this format: '01*********'",
)

def Phone_number_validate(phone_number):
    """
    It checks if the phone number is in the format of 011~019 followed by 8 digits
    :param phone_number: The phone number to validate
    :return: A match object or None
    """

    return re.match(r"^01[13-9]\d{8}$", phone_number)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=11, unique=True, blank=False, null=False)


