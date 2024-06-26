from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User, Customer


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
