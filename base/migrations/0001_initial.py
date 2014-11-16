# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('x_axis', models.CharField(max_length=255)),
                ('y_axis', models.CharField(max_length=255)),
                ('fixed', models.CharField(max_length=255)),
                ('fixed_type', models.CharField(max_length=255)),
                ('fixed_start', models.CharField(max_length=255)),
                ('fixed_end', models.CharField(max_length=255)),
                ('fixed_values', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
