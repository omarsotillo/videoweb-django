# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20151229_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 18, 23, 49, 439971), verbose_name=b'date published'),
        ),
    ]
