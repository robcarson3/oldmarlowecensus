# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-07 14:09


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0011_remove_contactform_guardian'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='guardian',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
