# Generated by Django 2.2.4 on 2019-08-08 02:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0003_auto_20190808_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='creator',
            field=models.CharField(default=' ', max_length=150),
        ),
        migrations.AlterField(
            model_name='room',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 8, 2, 24, 22, 913925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='room',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 8, 2, 24, 22, 913925, tzinfo=utc)),
        ),
    ]