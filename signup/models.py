from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pract import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name = 'profile',null=True)
    country = models.CharField(max_length=32, blank=True)

@receiver(post_save, sender=User)
def create_user_profile_token(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    api_token = models.CharField(max_length=100, null=True, blank=True)
    is_enabled = models.BooleanField(default=True)
    
