# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_auto_20180302_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proapprove',
            name='status',
            field=models.IntegerField(default=2, choices=[(0, '\u4e0d\u901a\u8fc7'), (1, '\u901a\u8fc7'), (2, '\u7b49\u5f85')]),
        ),
    ]
