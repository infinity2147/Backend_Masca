from django.db import models

class User(models.Model):
    ldap_id = models.CharField(max_length = 300)
    passcode = models.CharField(max_length = 300)
    Name = models.CharField(max_length = 300)
    DOB = models.CharField(max_length = 300)
    Branch = models.CharField(max_length = 300)
    Roll_no = models.CharField(max_length = 300)
    Hostel = models.CharField(max_length = 300)
    Room = models.CharField(max_length = 300)

    def __str__(self):
        return self.Roll_no

class Admin(models.Model):
    ldap_id = models.CharField(max_length = 50)
    passcode = models.CharField( max_length = 12 )
    Name = models.CharField(max_length = 300)
    DOB = models.CharField(max_length = 300)
    POR = models.CharField(max_length = 300)
    Admin_no = models.CharField(max_length = 300)
    Address = models.CharField(max_length = 500)


    def __str__(self):
        return self.Roll_no
