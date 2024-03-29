# Generated by Django 4.2.3 on 2024-02-27 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0129_delete_eventbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('phoneNo', models.TextField(max_length=10)),
                ('numOfcandidate', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=300)),
                ('time', models.TimeField()),
            ],
        ),
    ]
