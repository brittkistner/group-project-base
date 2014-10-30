# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuPageModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('page_url', models.CharField(max_length=500, null=True, blank=True)),
                ('page_number', models.CharField(max_length=5, null=True, blank=True)),
                ('page_down', models.CharField(max_length=5, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
