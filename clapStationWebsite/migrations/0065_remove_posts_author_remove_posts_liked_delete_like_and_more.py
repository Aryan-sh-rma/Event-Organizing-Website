# Generated by Django 4.2.3 on 2024-01-12 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0064_user_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='author',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='liked',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='posts',
        ),
    ]
