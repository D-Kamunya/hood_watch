# Generated by Django 3.1.2 on 2020-10-31 18:25

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='neighbourhood',
            options={'ordering': ['create_at']},
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_photo',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
