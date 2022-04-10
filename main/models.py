from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=40)
    account_balance = models.CharField(max_length=20, null=True, blank=True, default=0.00)
    active_dep = models.CharField(max_length=20, null=True, blank=True)
    total_earning = models.CharField(max_length=20, null=True, blank=True)
    confirmation = models.CharField(max_length=20, null=True, blank=True, default=0.00)

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=10)

    def __str__(self):
        return f'deposit of {self.amount} by {self.user.full_name}'

class Confirm(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
