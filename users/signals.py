from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()

@receiver(pre_save, sender=User)
def set_superuser_role(sender, instance, **kwargs):
    if instance.is_superuser:
        instance.role = 'ADMIN'
