# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_auto_20150331_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='process',
            field=models.CharField(default=None, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='domain',
            name='domain_name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ip',
            name='addr',
            field=models.IPAddressField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='nb',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
