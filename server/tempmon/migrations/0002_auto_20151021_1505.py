# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tempmon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DewPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('data', models.FloatField()),
                ('dt', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RenameField(
            model_name='humidity',
            old_name='date',
            new_name='data',
        ),
    ]
