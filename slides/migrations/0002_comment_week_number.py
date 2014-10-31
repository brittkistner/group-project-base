# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='week_number',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
    ]
