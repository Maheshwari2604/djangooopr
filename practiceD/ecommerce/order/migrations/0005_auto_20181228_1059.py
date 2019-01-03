# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-28 10:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20181226_0701'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0004_auto_20181228_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_id', models.CharField(max_length=120, unique=True)),
                ('status', models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='STARTED', max_length=120)),
                ('sub_total', models.DecimalField(decimal_places=2, default=19.99, max_digits=10)),
                ('tax_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('final_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='usr',
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]