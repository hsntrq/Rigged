# Generated by Django 3.1.7 on 2021-03-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210315_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.CharField(default='HasanNaseem', max_length=50),
        ),
    ]
