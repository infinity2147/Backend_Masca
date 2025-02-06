from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator 
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

# Custom validator for email
def validate_iitb_email(value):
    # Check if the email ends with '@iitb.ac.in'
    if not value.endswith('@iitb.ac.in'):
        raise ValidationError('Email must end with @iitb.ac.in')


class User(AbstractUser):
    username= models.EmailField(unique=True,validators=[validate_iitb_email],null =False,blank=False)
    password = models.CharField(max_length = 20 , validators=[
            MinLengthValidator(8, 'the field must contain at least 8 characters')
            ])
    profile_photo = models.ImageField(upload_to='profile_photo/',default='profile_photo/default-avatar-profile-icon-social-media-user-photo-in-flat-style-vector.jpg' )
    Name = models.CharField(max_length = 100)
    DOB = models.DateField(default=date.today)
    Branch = models.CharField(max_length = 30)
    Roll_no = models.CharField(max_length = 10)
    Address = models.CharField(max_length = 500)

    groups = models.ManyToManyField(
    'auth.Group', 
    related_name='user_groups'  # Renaming it for User
)
    user_permissions = models.ManyToManyField(
    'auth.Permission', 
    related_name='user_permissions'  # Renaming it for User
)
    
    def save(self, *args, **kwargs):
        """Hash password before saving."""
        if self.password and not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

        # Automatically add the user to the "User" group
        user_group, _ = Group.objects.get_or_create(name="User")
        self.groups.add(user_group)

    def __str__(self):
        return self.Roll_no

class lib_Admin(AbstractUser):
    username = models.EmailField(unique=True,validators=[validate_iitb_email],null =False,blank=False)
    password = models.CharField(max_length = 20 , validators=[
            MinLengthValidator(8, 'the field must contain at least 8 characters')
            ])
    profile_photo = models.ImageField(upload_to='profile_photo/',default='profile_photo/default-avatar-profile-icon-social-media-user-photo-in-flat-style-vector.jpg' )
    Name = models.CharField(max_length = 100)
    DOB = models.DateField(default=date.today)
    POR = models.CharField(max_length = 30)
    lib_Admin_no = models.CharField(max_length = 10)
    Address = models.CharField(max_length = 500)
    groups = models.ManyToManyField(
    'auth.Group', 
    related_name='lib_admin_groups'  # Renaming it for lib_Admin
)
    user_permissions = models.ManyToManyField(
    'auth.Permission', 
    related_name='lib_admin_permissions'  # Renaming it for lib_Admin
)
    def save(self, *args, **kwargs):
        """Hash password before saving."""
        if self.password and not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
         # Now assign the group
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        self.groups.add(admin_group)  
    
    def __str__(self):
        return self.lib_Admin_no
