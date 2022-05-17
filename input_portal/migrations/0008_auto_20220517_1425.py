# Generated by Django 3.2 on 2022-05-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_portal', '0007_auto_20220517_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='results_info',
            name='sprint_king',
            field=models.CharField(default='', max_length=65),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='results_data',
            name='grid',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sprint_data',
            name='grid',
            field=models.CharField(max_length=2),
        ),
    ]
