# Generated by Django 3.0.5 on 2021-05-01 02:29

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0009_merge_20210421_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=12, region=None),
        ),
    ]