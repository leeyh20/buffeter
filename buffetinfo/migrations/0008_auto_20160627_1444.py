# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buffetinfo', '0007_auto_20160627_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buffet',
            name='location',
            field=models.CharField(choices=[('Jurong East', 'Jurong East'), ('Bukit Batok', 'Bukit Batok'), ('Bukit Gombak', 'Bukit Gombak'), ('Choa Chu Kang', 'Choa Chu Kang'), ('Yew Tee', 'Yew Tee'), ('Kranji', 'Kranji'), ('Marsiling', 'Marsiling'), ('Woodlands', 'Woodlands'), ('Admiralty', 'Admiralty'), ('Sembawang', 'Sembawang'), ('Yishun', 'Yishun'), ('Khatib', 'Khatib'), ('Yio Chu Kang', 'Yio Chu Kang'), ('Ang Mo Kio', 'Ang Mo Kio'), ('Bishan', 'Bishan'), ('Braddell', 'Braddell'), ('Toa Payoh', 'Toa Payoh'), ('Novena', 'Novena'), ('Newton', 'Newton'), ('Orchard', 'Orchard'), ('Somerset', 'Somerset'), ('Dhoby Ghaut', 'Dhoby Ghaut'), ('City Hall', 'City Hall'), ('Raffles Place', 'Raffles Place'), ('Marina Bay', 'Marina Bay'), ('Marina South Pier', 'Marina South Pier')], max_length=200),
        ),
    ]
