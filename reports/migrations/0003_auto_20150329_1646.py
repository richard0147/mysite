# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_remove_node_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mrtg_images',
            name='path',
        ),
        migrations.AddField(
            model_name='mrtg_images',
            name='picture',
            field=models.ImageField(default=1, upload_to=b'mrtg'),
            preserve_default=False,
        ),
    ]
