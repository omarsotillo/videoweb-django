# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151221_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='tags',
            field=models.TextField(default=b'video'),
        ),
    ]
