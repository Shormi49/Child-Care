from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="children")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='children_images/')
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

