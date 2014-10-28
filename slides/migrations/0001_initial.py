# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
<<<<<<< HEAD
                ('image', models.ImageField(null=True, upload_to=b'media/user_photo', blank=True)),
=======
                ('image', models.ImageField(null=True, upload_to=b'user_photo', blank=True)),
>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e
                ('name', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(null=True, upload_to=b'media/comment_attachment', blank=True)),
                ('uuid', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
=======
>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
<<<<<<< HEAD
                ('week_number', models.IntegerField()),
                ('day', models.CharField(max_length=5)),
                ('slide_set', models.IntegerField()),
                ('slide_number', models.IntegerField()),
=======
>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e
                ('user', models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
<<<<<<< HEAD
        migrations.AddField(
            model_name='attachment',
            name='comment',
            field=models.ForeignKey(related_name='attachments', blank=True, to='slides.Comment', null=True),
            preserve_default=True,
        ),
=======
>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e
    ]
