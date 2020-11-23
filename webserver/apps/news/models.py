# built-in python modules
import uuid

# built-in django modules
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class New(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    publication = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-publication']

    def __str__(self):
        return f'{self.author.username}: {self.content}'
