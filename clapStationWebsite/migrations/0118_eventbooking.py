# Generated by Django 4.2.3 on 2024-02-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0117_delete_eventbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('phoneNo', models.TextField(max_length=10)),
                ('numOfPeople', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('Which_type_of_Booking', models.TextField()),
            ],
        ),
    ]
