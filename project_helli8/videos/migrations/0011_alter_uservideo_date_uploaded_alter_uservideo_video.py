# Generated by Django 4.0.3 on 2022-07-21 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_alter_uservideo_date_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 10, 49, 11, 18666)),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='video',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]