# Generated by Django 3.1 on 2020-09-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0029_auto_20200924_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='edited_by',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
