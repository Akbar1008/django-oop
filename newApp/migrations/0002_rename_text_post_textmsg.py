# Generated by Django 5.0.2 on 2024-02-24 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='textmsg',
        ),
    ]
