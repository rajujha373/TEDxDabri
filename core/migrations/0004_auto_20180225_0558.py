# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_text_coming_soon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='coming_soon',
        ),
        migrations.AddField(
            model_name='speaker',
            name='coming_soon',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
