# Generated by Django 4.0.3 on 2022-07-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='./profile/default_pfp.jpeg', null=True, upload_to='profile/'),
        ),
    ]
