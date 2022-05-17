# Generated by Django 3.2 on 2022-05-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_portal', '0009_alter_alltime_leaderboard_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='alltime_leaderboard',
            name='sprint_king',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alltime_leaderboard',
            name='sprint_medals',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alltime_leaderboard',
            name='sprints',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]