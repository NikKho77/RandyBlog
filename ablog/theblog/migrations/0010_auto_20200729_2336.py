# Generated by Django 3.0.8 on 2020-07-29 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_welcomepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='adress',
            new_name='address',
        ),
    ]
