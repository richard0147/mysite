# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attact_node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nb', models.IntegerField()),
                ('max_qps', models.IntegerField()),
                ('average_qps', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dnsla_images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_name', models.CharField(max_length=100)),
                ('registrant', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addr', models.IPAddressField()),
                ('origin', models.CharField(max_length=50)),
                ('type', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mrtg_images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nb', models.IntegerField()),
                ('abbr', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField()),
                ('content', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Qps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_id', models.IntegerField(default=0)),
                ('end_time', models.DateTimeField()),
                ('in_qps', models.IntegerField(default=0)),
                ('out_qps', models.IntegerField(default=0)),
                ('is_attact', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Qps_snapshots',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField()),
                ('persion', models.CharField(max_length=100)),
                ('abstract', models.CharField(max_length=1000)),
                ('type', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('max_qps', models.IntegerField()),
                ('is_end', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='qps',
            name='snap_id',
            field=models.ForeignKey(to='reports.Qps_snapshots'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='report',
            field=models.ForeignKey(related_name='processes', to='reports.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='node',
            name='report',
            field=models.ManyToManyField(related_name='nodes', to='reports.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mrtg_images',
            name='report',
            field=models.ForeignKey(related_name='mrtg_images', to='reports.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ip',
            name='report',
            field=models.ManyToManyField(related_name='ips', to='reports.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='report',
            field=models.ManyToManyField(related_name='domains', to='reports.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dnsla_images',
            name='report',
            field=models.ForeignKey(related_name='dnsla_images', to='reports.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attact_node',
            name='report',
            field=models.ForeignKey(related_name='attact_nodes', to='reports.Report'),
            preserve_default=True,
        ),
    ]
