# Generated by Django 4.2.3 on 2024-02-28 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0156_eventbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventbooking',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventimage',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Eventbooking',
        ),
        migrations.DeleteModel(
            name='EventImage',
        ),
    ]
