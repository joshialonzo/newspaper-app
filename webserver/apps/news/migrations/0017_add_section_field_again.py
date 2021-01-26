# Generated by Django 3.1.3 on 2020-12-21 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_add_section_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='section',
            field=models.CharField(choices=[('local', 'Yucatán'), ('national', 'México'), ('international', 'International'), ('entertainment', 'Entertainment')], default='local', max_length=20),
        ),
    ]