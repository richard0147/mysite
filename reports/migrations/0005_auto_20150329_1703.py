# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20150329_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrtg_images',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'mrtg'),
            preserve_default=True,
        ),
    ]
