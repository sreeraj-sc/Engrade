# Generated by Django 3.2.7 on 2024-03-08 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fencing', '0007_tournament_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament_register',
            name='status',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
