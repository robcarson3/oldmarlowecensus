# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-06 20:31


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0010_auto_20180806_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='guardian',
        ),
    ]
