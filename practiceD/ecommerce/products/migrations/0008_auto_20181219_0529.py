# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-19 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181218_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.FileField(upload_to=b''),
        ),
    ]
