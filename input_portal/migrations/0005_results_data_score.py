# Generated by Django 3.2 on 2022-04-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_portal', '0004_rename_result_info_results_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='results_data',
            name='score',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
