# Generated by Django 3.2.7 on 2024-03-07 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fencing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tournament_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=150)),
                ('start_time', models.DateField(max_length=150)),
                ('status', models.DateField(max_length=150)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fencing.tournamenttable')),
            ],
        ),
    ]