# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buffetinfo', '0011_auto_20160627_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buffet',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
    ]
