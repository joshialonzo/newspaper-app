# Generated by Django 3.1.5 on 2021-01-26 18:53

import apps.news.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_add_section_field_again'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='image',
            field=models.ImageField(blank=True, upload_to=apps.news.models.media_resource_folder),
        ),
    ]
