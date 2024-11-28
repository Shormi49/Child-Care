# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    transaction_id = models.CharField(max_length=50)
    #amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional donation amount
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation by {self.name} - {self.transaction_id}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username



