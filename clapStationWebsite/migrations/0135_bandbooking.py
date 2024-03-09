# Generated by Django 4.2.3 on 2024-02-27 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0134_eventbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bandbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('phoneNo', models.TextField(max_length=10)),
                ('numOfcandidate', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=300)),
                ('time', models.DateTimeField()),
                ('bands', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clapStationWebsite.create_bands')),
            ],
        ),
    ]