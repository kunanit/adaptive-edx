# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0004_activity_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequenceitem',
            name='method',
            field=models.CharField(blank=True, default=b'', max_length=200),
        ),
    ]
