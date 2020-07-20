from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_age = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

