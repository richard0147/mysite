# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0014_auto_20150410_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='addr',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]
