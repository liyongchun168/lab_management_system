# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20180302_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proapprove',
            name='project',
            field=models.ForeignKey(blank=True, to='lab.Project', null=True),
        ),
        migrations.AlterField(
            model_name='proapprove',
            name='status',
            field=models.IntegerField(default=1, choices=[(0, '\u4e0d\u901a\u8fc7'), (1, '\u7b49\u5f85'), (2, '\u901a\u8fc7')]),
        ),
    ]
