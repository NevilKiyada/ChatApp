# Generated by Django 5.0.6 on 2024-05-21 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_userprofile_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]