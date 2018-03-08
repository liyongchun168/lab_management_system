# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0011_auto_20180304_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodborrow',
            name='status',
            field=models.IntegerField(default=2, choices=[(0, '\u4e0d\u901a\u8fc7'), (1, '\u901a\u8fc7'), (2, '\u7b49\u5f85')]),
        ),
        migrations.AlterField(
            model_name='goodborrow',
            name='end_t',
            field=models.DateField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='goodborrow',
            name='num',
            field=models.IntegerField(default=1, verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='goodborrow',
            name='start_t',
            field=models.DateField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', blank=True),
        ),
    ]
