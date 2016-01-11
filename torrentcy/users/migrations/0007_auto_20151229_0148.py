# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20151227_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 1, 48, 0, 449048), verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(upload_to=b'static'),
        ),
    ]
