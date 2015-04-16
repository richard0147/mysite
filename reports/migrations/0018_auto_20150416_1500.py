# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0017_auto_20150414_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qps',
            name='snap_id',
        ),
        migrations.DeleteModel(
            name='Qps_snapshots',
        ),
    ]
