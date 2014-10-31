# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0003_auto_20141031_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='day',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
