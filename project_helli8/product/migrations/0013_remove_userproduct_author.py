# Generated by Django 4.0.3 on 2022-08-18 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_userproduct_mani'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproduct',
            name='author',
        ),
    ]
