# Generated by Django 3.1.3 on 2020-12-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_new_model_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
