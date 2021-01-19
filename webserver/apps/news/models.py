# built-in python modules
import datetime
import locale
import uuid

# built-in django modules
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# third-party django modules
from ckeditor.fields import RichTextField

# Create your models here.


class New(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    SECTION_CHOICES = (
        ('local', 'Yucatán'),
        ('national', 'México'),
        ('international', 'International'),
        ('entertainment', 'Entertainment'),
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
    section = models.CharField(choices=SECTION_CHOICES, default='local', max_length=20)

    class Meta:
        ordering = ['-publication']

    def __str__(self):
        return f'{self.author.username}: {self.content}'

    def get_first_image(self):
        return self.resource_set.first() if self.resource_set else None

    def get_color(self):
        colors = {
            'local': 'danger',
            'national': 'warning',
            'international': 'info',
            'entertainment': 'link',
        }
        return colors[str(self.section)]

    def get_date_string(self):
        MONTHS = {
            1: 'Enero', 2: 'Febrero',
            3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio',
            7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre',
            11: 'Noviembre', 12: 'Diciembre',
        }
        new_date = self.created_at
        new_day = new_date.day
        new_month = MONTHS[new_date.month]
        new_year = new_date.year
        new_hours = new_date.hour
        new_minutes = new_date.minute
        date_str = f'{new_day} de {new_month} de {new_year}'
        time_str = f'{new_hours}:{new_minutes}'
        space = ' · '
        return date_str + space + time_str


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
