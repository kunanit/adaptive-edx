# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_auto_20160928_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='max_points',
        ),
        migrations.AddField(
            model_name='activity',
            name='dependencies',
            field=models.ManyToManyField(blank=True, to='module.Activity'),
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[(b'problem', b'problem'), (b'html', b'html')], default='problem', max_length=100),
            preserve_default=False,
        ),
    ]
