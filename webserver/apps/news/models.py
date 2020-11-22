# built-in django modules
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class New(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'
