# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TimelyWarning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('permanent_url', models.URLField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('location', models.ManyToManyField(to='alert.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('warning_name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='timelywarning',
            name='warning_type',
            field=models.ManyToManyField(to='alert.Warning'),
        ),
    ]
