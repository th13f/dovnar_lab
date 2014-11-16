# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='fixed_values',
            new_name='fixed_str',
        ),
        migrations.RemoveField(
            model_name='report',
            name='fixed_end',
        ),
        migrations.RemoveField(
            model_name='report',
            name='fixed_start',
        ),
    ]
