# Generated by Django 3.0.5 on 2020-04-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='avatars')),
            ],
        ),
    ]
