# built-in python modules
import datetime
import uuid

# built-in django modules
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# third-party django modules
from ckeditor.fields import RichTextField

# Create your models here.


class Section(models.Model):
    COLOR_CHOICES = (
        ('warning', 'Warning'),
        ('danger', 'Danger'),
        ('info', 'Info'),
        ('success', 'Success'),
        ('link', 'Link'),
        ('primary', 'Primary'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, null=True)
    color = models.CharField(choices=COLOR_CHOICES, default='info', max_length=20)


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
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    publication = models.DateTimeField(default=timezone.now)
    content = RichTextField(blank=True, null=True)
    section = models.ForeignKey(Section,
                                on_delete=models.CASCADE,
                                related_name='news',
                                null=True, blank=True)

    class Meta:
        ordering = ['-publication']

    def __str__(self):
        return f'{self.author.username}: {self.content}'

    def get_first_image(self):
        return self.resource_set.first() if self.resource_set else None


def media_resource_folder(instance, filename):
    """file will be uploaded to MEDIA_ROOT/<username>/2020/09/02/<new_filename>
    :param instance: resource instance with a user
    :param filename: filename of the image
    :return: path of the new filename
    """
    today = datetime.date.today()
    today_path = today.strftime('%Y/%m/%d')
    extension = filename.split('.')[-1].lower()
    return f'resources/{instance.author.username}/{today_path}/{uuid.uuid4()}.{extension}'


class Resource(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media_resource_folder)
    youtube_video = models.URLField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.new.title
