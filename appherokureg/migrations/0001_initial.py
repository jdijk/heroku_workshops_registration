# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=300)),
                ('company', models.CharField(max_length=300)),
                ('role', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=100)),
                ('attended', models.BooleanField(default=False)),
                ('reg_key', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(unique=True, max_length=300)),
                ('dateandtime', models.DateTimeField()),
                ('title', models.CharField(max_length=300)),
                ('picture_url', models.URLField()),
                ('location', models.CharField(max_length=300)),
                ('long_description', models.TextField()),
            ],
        ),        
    ]
