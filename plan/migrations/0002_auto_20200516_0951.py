# Generated by Django 3.0.5 on 2020-05-16 05:21

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=75, size=[100, 100], upload_to='avatars'),
        ),
    ]
