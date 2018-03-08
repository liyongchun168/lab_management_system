# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0010_auto_20180304_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='user_borrowed',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='lab.GoodBorrow', blank=True),
        ),
    ]
