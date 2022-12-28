from django.db import models
from django.contrib.auth.models import User

class User_address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, blank=False)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=200)
    
# Create your models here.
