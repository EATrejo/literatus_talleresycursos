# Generated by Django 5.1.3 on 2024-11-29 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
