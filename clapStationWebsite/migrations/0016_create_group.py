# Generated by Django 4.2.3 on 2023-12-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0015_event_detail_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(default='', upload_to='creategroup/image')),
                ('groupname', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
