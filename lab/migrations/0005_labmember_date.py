# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20180224_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='labmember',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 24, 10, 16, 43, 276005, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
