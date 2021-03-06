# Generated by Django 4.0.3 on 2022-07-19 06:39

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import podcast.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0009_alter_userproduct_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('voice', models.FileField(null=True, upload_to=podcast.models.get_voice_ext, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])])),
                ('date_uploaded', models.DateTimeField(default=datetime.datetime(2022, 7, 19, 11, 9, 12, 695211))),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcasts', to='product.userproduct')),
            ],
        ),
    ]
