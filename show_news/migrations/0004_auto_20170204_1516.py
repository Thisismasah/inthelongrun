# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_news', '0003_auto_20170122_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='NA', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sources',
            name='author',
            field=models.CharField(default='NA', max_length=250),
            preserve_default=False,
        ),
    ]
