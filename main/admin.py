from django.contrib import admin
from .models import UserProfile,Donation

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Donation)