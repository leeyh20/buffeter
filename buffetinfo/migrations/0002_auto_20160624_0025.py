# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buffetinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buffet',
            old_name='updated_date',
            new_name='published_date',
        ),
    ]