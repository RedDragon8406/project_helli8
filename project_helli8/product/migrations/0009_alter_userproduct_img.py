# Generated by Django 4.0.3 on 2022-07-19 06:39

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_userproduct_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproduct',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.get_filename_ext),
        ),
    ]
