# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0015_auto_20150413_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='attact_node',
            name='dsnla_json',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
