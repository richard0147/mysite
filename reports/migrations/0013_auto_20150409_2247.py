# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0012_auto_20150409_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='origin',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
    ]
