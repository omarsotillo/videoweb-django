# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.FileField(upload_to=b'uploads')),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('description', models.CharField(max_length=250)),
                ('views', models.IntegerField(default=0)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
