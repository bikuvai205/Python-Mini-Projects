from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    employee_id = models.IntegerField(unique= True)
    department = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    
    def __str__(self):
      return self.user.username
