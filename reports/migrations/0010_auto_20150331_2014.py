# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20150329_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='create_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='end_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='start_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
