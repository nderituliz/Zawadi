from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from pyuploadcare.dj.models import ImageField

class Profile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = ImageField(manual_crop='500x500')
    bio = models.TextField(default="Here is my bio...")
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.username.username
