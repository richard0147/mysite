# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20150329_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrtg_images',
            name='report',
            field=models.ForeignKey(related_name='mrtg_images', default=None, to='reports.Report'),
            preserve_default=True,
        ),
    ]
