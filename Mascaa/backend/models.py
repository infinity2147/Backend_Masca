from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator 
from django.core.exceptions import ValidationError
import re

# Custom validator for email
def validate_iitb_email(value):
    # Check if the email ends with '@iitb.ac.in'
    if not value.endswith('@iitb.ac.in'):
        raise ValidationError('Email must end with @iitb.ac.in')


class User(models.Model):
    ldap_id = models.EmailField(unique=True,validators=[validate_iitb_email],null =True)
    passcode = models.CharField(max_length = 20 , validators=[
            MinLengthValidator(8, 'the field must contain at least 8 characters')
            ])
    profile_photo = models.ImageField(upload_to='profile_photo/',default='profile_photo/default-avatar-profile-icon-social-media-user-photo-in-flat-style-vector.jpg' )
    Name = models.CharField(max_length = 100)
    DOB = models.DateField(default=date.today)
    Branch = models.CharField(max_length = 30)
    Roll_no = models.CharField(max_length = 10)
    Hostel = models.CharField(max_length = 10)
    Room = models.PositiveIntegerField

    REQUIRED_FIELDS = ['ldap_id'] #to tackle error
    def __str__(self):
        return self.Roll_no

class lib_Admin(models.Model):
    ldap_id = models.EmailField(unique=True,validators=[validate_iitb_email],null=True)
    passcode = models.CharField(max_length = 20 , validators=[
            MinLengthValidator(8, 'the field must contain at least 8 characters')
            ])
    profile_photo = models.ImageField(upload_to='profile_photo/',default='profile_photo/default-avatar-profile-icon-social-media-user-photo-in-flat-style-vector.jpg' )
    Name = models.CharField(max_length = 100)
    DOB = models.DateField(default=date.today)
    POR = models.CharField(max_length = 30)
    lib_Admin_no = models.CharField(max_length = 10)
    Address = models.CharField(max_length = 500)


    def __str__(self):
        return self.lib_Admin_no
