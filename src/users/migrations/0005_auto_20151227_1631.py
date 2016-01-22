# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151227_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 27, 16, 31, 9, 116032), verbose_name=b'date published'),
        ),
    ]
