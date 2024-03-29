# Generated by Django 4.2.3 on 2024-02-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0109_blogcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAtutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Profession_title', models.CharField(max_length=100)),
                ('Fee', models.TextField()),
                ('Status', models.CharField(max_length=50)),
                ('SessionDays', models.CharField(max_length=300)),
                ('social_links', models.CharField(blank=True, max_length=100, null=True)),
                ('social_links1', models.CharField(blank=True, max_length=100, null=True)),
                ('social_links2', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
