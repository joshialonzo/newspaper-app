# Generated by Django 3.1.3 on 2020-11-23 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_user_to_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': []},
        ),
        migrations.RemoveField(
            model_name='new',
            name='timestamp',
        ),
    ]
