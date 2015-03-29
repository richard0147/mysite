# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20150329_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrtg_images',
            name='picture',
            field=models.ImageField(upload_to=b'mrtg'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mrtg_images',
            name='report',
            field=models.ForeignKey(related_name='mrtg_images', to='reports.Report'),
            preserve_default=True,
        ),
    ]
