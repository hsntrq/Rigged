# Generated by Django 3.0.5 on 2021-04-18 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0004_auto_20210419_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirm_password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]