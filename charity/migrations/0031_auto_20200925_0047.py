# Generated by Django 3.1 on 2020-09-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0030_auto_20200924_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]