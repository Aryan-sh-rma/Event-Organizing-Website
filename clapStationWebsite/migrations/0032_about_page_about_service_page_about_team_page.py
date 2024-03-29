# Generated by Django 4.2.3 on 2024-01-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0031_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about_images/')),
            ],
        ),
        migrations.CreateModel(
            name='About_service_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about_images/')),
            ],
        ),
        migrations.CreateModel(
            name='About_team_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=250)),
                ('occuption', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='about_images/')),
            ],
        ),
    ]
