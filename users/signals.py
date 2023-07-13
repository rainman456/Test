from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_wallet(sender, created, instance, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)