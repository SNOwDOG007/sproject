# Generated by Django 3.1 on 2020-09-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0014_auto_20200917_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='joined_from',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
