# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_desk'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='desk',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='booking.Desk'),
            preserve_default=False,
        ),
    ]