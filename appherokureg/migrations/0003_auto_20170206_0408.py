# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appherokureg', '0002_workshop_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='picture_url',
            field=models.URLField(blank=True),
        ),
    ]
