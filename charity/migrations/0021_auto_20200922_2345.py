# Generated by Django 3.1 on 2020-09-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0020_auto_20200922_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='joined_from',
            field=models.DateField(auto_now=True),
        ),
    ]
