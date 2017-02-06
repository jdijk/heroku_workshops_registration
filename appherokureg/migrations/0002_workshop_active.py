# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appherokureg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='workshop',
            field=models.ForeignKey(to='appherokureg.Workshop'),
        ),
    ]
