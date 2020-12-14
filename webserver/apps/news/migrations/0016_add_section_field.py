# Generated by Django 3.1.3 on 2020-12-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_remove_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='section',
            field=models.CharField(choices=[('local', 'Yucatán'), ('national', 'México'), ('international', 'Internacional'), ('entertainment', 'Entretenimiento')], default='local', max_length=20),
        ),
    ]
