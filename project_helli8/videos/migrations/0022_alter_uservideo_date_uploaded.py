# Generated by Django 4.0.3 on 2022-07-25 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0021_alter_uservideo_date_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 25, 13, 57, 41, 521176)),
        ),
    ]
