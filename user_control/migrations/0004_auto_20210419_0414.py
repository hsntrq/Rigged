# Generated by Django 3.0.5 on 2021-04-18 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0003_auto_20210419_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contact',
            field=models.CharField(default='', max_length=12),
        ),
    ]