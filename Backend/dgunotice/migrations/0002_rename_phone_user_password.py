# Generated by Django 4.1.6 on 2023-05-20 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dgunotice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='password',
        ),
    ]
