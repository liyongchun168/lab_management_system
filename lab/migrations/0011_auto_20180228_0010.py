# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0010_auto_20180227_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectteam',
            name='users',
            field=models.ManyToManyField(related_name='join_project', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
