# Generated by Django 5.1 on 2024-08-29 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='max_participants',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
