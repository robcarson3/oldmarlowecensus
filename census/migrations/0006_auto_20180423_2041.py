# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-23 20:41


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0005_auto_20180327_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='Marginalia',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
