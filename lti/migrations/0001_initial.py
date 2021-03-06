# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LtiParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(default='')),
                ('lis_outcome_service_url', models.CharField(default='', max_length=300)),
                ('lis_result_sourcedid', models.CharField(default='', max_length=300)),
                ('oauth_consumer_key', models.CharField(default='', max_length=300)),
                ('user_id', models.CharField(default='', max_length=300)),
                ('lis_person_sourcedid', models.CharField(default='', max_length=300)),
                ('user_module', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='module.UserModule')),
            ],
            options={
                'verbose_name': 'LTI Parameters',
                'verbose_name_plural': 'LTI Parameters',
            },
        ),
    ]
