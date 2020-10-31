from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    profile = Profile(user=instance)
    profile.save()



# @receiver(post_save,sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save,sender=User)
# def create_profile(sender,**kwargs ):
#     if kwargs['created']:
#         user_profile=Profile(user=kwargs['instance'])
#         user_profile.save()

# post_save.connect(create_profile, sender=User)

# @receiver(post_save,sender=User)
# def save_profile(sender,instance,**kwargs):
#     instance.profile.save()

