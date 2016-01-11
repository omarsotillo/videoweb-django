# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_videos_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name=b'date published'),
        ),
    ]
