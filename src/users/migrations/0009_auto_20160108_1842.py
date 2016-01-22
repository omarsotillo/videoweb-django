# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20151229_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='videos',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 8, 18, 42, 48, 705969), verbose_name=b'date published'),
        ),
    ]
