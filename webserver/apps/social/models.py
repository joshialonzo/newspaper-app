# built-in python modules
import uuid

# built-in django modules
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


def media_profile_folder(instance, filename):
    """file will be uploaded to MEDIA_ROOT/user_<id>/<new_filename>
    :param instance: profile instance with a user
    :param filename: filename of the image
    :return: path of the new filename
    """
    extension = filename.split('.')[-1].lower()
    user_id = instance.user.id
    new_filename = f'{user_id}.{extension}'
    return f'profiles/{instance.user.username}/{new_filename}'


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=media_profile_folder, default='batman.png')
    objects = models.Manager()

    def __str__(self):
        return f'Perfil de {self.user.username}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
