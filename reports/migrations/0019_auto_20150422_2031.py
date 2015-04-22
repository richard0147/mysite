# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0018_auto_20150416_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process',
            name='report',
        ),
        migrations.DeleteModel(
            name='Process',
        ),
    ]
