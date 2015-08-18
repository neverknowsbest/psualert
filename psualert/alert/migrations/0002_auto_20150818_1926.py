# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Warning',
            new_name='WarningType',
        ),
        migrations.RenameField(
            model_name='warningtype',
            old_name='warning_name',
            new_name='warning_type',
        ),
        migrations.AlterField(
            model_name='timelywarning',
            name='permanent_url',
            field=models.URLField(unique=True),
        ),
    ]
