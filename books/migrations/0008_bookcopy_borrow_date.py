# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20170411_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcopy',
            name='borrow_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]