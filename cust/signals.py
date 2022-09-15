from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from .models import Customer

account_name = get_user_model()

@receiver(post_save, sender=account_name)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(account_name=instance)