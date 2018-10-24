# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 18:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0007_auto_20180612_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibrarianEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'trusted emails',
            },
        ),
    ]
