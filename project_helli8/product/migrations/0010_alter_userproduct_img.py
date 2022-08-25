# Generated by Django 4.0.3 on 2022-07-21 06:19

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_userproduct_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproduct',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path),
        ),
    ]