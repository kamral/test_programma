# Generated by Django 2.2.4 on 2020-10-20 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flowers',
            name='slug',
        ),
    ]