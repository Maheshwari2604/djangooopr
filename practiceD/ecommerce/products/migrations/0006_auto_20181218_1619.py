# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181218_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
