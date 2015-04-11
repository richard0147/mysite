# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0013_auto_20150409_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mrtg_images',
            name='report',
        ),
        migrations.DeleteModel(
            name='Mrtg_images',
        ),
        migrations.AddField(
            model_name='attact_node',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'mrtg'),
            preserve_default=False,
        ),
    ]
