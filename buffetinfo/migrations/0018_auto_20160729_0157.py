# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buffetinfo', '0017_auto_20160721_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='reviews'),
        ),
    ]
