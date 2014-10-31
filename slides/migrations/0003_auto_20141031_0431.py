# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_comment_week_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slide_number',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='slide_set',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='week_number',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
