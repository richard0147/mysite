# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20150329_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnsla_images',
            name='picture',
            field=models.ImageField(upload_to=b'dnsla'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dnsla_images',
            name='report',
            field=models.ForeignKey(related_name='dnsla_images', to='reports.Report'),
            preserve_default=True,
        ),
    ]
