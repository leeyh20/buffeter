# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buffetinfo', '0015_auto_20160629_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='reviews/pics')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buffetinfo.Review')),
            ],
        ),
    ]