# Generated by Django 3.1.2 on 2020-10-31 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', pyuploadcare.dj.models.ImageField(blank=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('contact', models.CharField(blank=True, max_length=60)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
