# Generated by Django 4.1.6 on 2023-05-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dgunotice', '0002_pagetype_category_clink_alter_category_cname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='time_initial',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='category',
            name='time_remaining',
            field=models.IntegerField(default=1),
        ),
    ]
