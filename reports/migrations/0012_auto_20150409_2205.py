# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_auto_20150409_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='abstract',
            field=models.CharField(max_length=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='process',
            field=models.CharField(max_length=2000),
            preserve_default=True,
        ),
    ]
