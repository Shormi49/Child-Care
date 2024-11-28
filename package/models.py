from django.contrib.auth.models import User
from django.db import models

class Package(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages')
    PACKAGE_CHOICES = [
        ('premium', 'Premium'),
        ('medium', 'Medium'),
        ('casual', 'Casual'),
    ]
    package_type = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    transaction_id = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.package_type}"
