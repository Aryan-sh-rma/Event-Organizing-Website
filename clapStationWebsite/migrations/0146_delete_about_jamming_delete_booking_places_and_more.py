# Generated by Django 4.2.3 on 2024-02-28 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0145_delete_tutorcontact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About_jamming',
        ),
        migrations.DeleteModel(
            name='Booking_Places',
        ),
        migrations.DeleteModel(
            name='Jamming_channel',
        ),
        migrations.DeleteModel(
            name='Jamming_titles',
        ),
    ]