# Generated by Django 5.2.1 on 2025-05-22 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='email',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='password',
        ),
    ]
