# Generated by Django 3.2.7 on 2024-03-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fencing', '0008_tournament_register_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament_register',
            name='score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
