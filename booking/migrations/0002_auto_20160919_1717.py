# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desk',
            old_name='desk',
            new_name='desk_number',
        ),
    ]