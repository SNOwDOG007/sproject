# Generated by Django 3.1 on 2020-10-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0047_blog_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
