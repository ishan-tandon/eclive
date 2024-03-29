# Generated by Django 3.2 on 2022-04-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=32, unique=True)),
                ('driver_name', models.CharField(max_length=128)),
                ('team_color', models.CharField(max_length=7)),
                ('points', models.FloatField()),
                ('rank_override', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='alltime_leaderboard',
            name='championships',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
