# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_auto_20180225_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmember',
            name='grade',
            field=models.CharField(blank=True, max_length=4, choices=[(b'2014', '14\u7ea7'), (b'2015', '15\u7ea7'), (b'2016', '16\u7ea7'), (b'2017', '17\u7ea7')]),
        ),
    ]
