# Generated by Django 3.1.2 on 2020-10-31 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood'),
        ),
    ]
