# Generated by Django 4.2.3 on 2024-01-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0033_delete_about_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]
