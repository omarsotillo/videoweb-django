# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20151227_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 27, 16, 32, 33, 74745), verbose_name=b'date published'),
        ),
    ]
