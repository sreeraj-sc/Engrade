# Generated by Django 3.2.7 on 2024-03-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fencing', '0005_tournament_medals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament_medals',
            name='bronze',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tournament_medals',
            name='gold',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tournament_medals',
            name='silver',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tournament_medals',
            name='total',
            field=models.IntegerField(),
        ),
    ]
