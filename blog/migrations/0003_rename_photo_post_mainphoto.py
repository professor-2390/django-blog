# Generated by Django 3.2 on 2021-04-17 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='photo',
            new_name='mainPhoto',
        ),
    ]
