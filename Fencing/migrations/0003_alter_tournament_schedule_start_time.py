# Generated by Django 3.2.7 on 2024-03-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fencing', '0002_tournament_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament_schedule',
            name='start_time',
            field=models.TimeField(max_length=150),
        ),
    ]
