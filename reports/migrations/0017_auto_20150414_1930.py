# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0016_attact_node_dsnla_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dnsla_images',
            name='report',
        ),
        migrations.DeleteModel(
            name='Dnsla_images',
        ),
        migrations.RemoveField(
            model_name='attact_node',
            name='dsnla_json',
        ),
        migrations.AddField(
            model_name='attact_node',
            name='dnsla_json',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
