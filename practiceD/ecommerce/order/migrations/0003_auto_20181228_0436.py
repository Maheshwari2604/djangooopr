# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-28 04:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20181227_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cart_id',
            new_name='cart',
        ),
    ]
