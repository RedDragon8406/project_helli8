# Generated by Django 4.0.3 on 2022-07-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_userproduct_categories'),
        ('profiles', '0002_userprofile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorite',
            field=models.ManyToManyField(blank=True, to='product.userproduct'),
        ),
    ]