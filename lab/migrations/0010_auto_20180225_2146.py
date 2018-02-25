# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0009_auto_20180225_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmember',
            name='name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='labmember',
            name='role',
            field=models.IntegerField(choices=[(2, '\u5b66\u751f'), (1, '\u8001\u5e08')]),
        ),
    ]
