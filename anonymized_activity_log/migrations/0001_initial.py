# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user', models.CharField(verbose_name='user', max_length=256)),
                ('request_url', models.CharField(verbose_name='url', max_length=256)),
                ('request_method', models.CharField(verbose_name='http method', max_length=10)),
                ('response_code', models.CharField(verbose_name='response code', max_length=3)),
                ('datetime', models.DateTimeField(verbose_name='datetime', default=django.utils.timezone.now)),
                ('extra_data', models.TextField(blank=True, verbose_name='extra data', null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, verbose_name='user IP', null=True)),
                ('session_id', models.CharField(null=True, max_length=256)),
                ('request_path', models.TextField()),
                ('request_query_string', models.TextField()),
                ('request_vars', models.TextField()),
                ('request_secure', models.BooleanField(default=False)),
                ('request_ajax', models.BooleanField(default=False)),
                ('request_meta', models.TextField(blank=True, null=True)),
                ('view_function', models.CharField(max_length=256)),
                ('view_doc_string', models.TextField(blank=True, null=True)),
                ('view_args', models.TextField()),
            ],
            options={
                'verbose_name': 'activity log',
            },
        ),
    ]
