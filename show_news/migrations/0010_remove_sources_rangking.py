# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_news', '0009_auto_20170204_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sources',
            name='rangking',
        ),
    ]
