# Generated by Django 5.1.3 on 2024-12-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tertulias', '0005_remove_tertulia_tertulia_lugares_disponibles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tertulia',
            name='tertulia_lugares',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
