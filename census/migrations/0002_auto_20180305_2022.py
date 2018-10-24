# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-05 20:22


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='bibliography',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Bartlett1916_Notes',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Bartlett1939_Notes',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Binder',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Binding',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Bookplate',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Bookplate_Location',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Condition',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Lee_Notes',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Local_Notes',
            field=models.CharField(blank=True, default=None, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Marginalia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Shelfmark',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='prov_info',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='thumbnail_URL',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='edition',
            name='Edition_format',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='edition',
            name='Edition_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Variant_Description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='notes',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
