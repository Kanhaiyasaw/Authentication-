from django.db import models
from django.contrib.auth.models import User # import the User model in-built model

# it is class of signup the user detail
class User_address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, blank=False)# relation to the User table
    address = models.CharField(max_length=250)
    profile_image = models.ImageField(upload_to='media', blank=True)
    city = models.CharField(max_length=200)
    
