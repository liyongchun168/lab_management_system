# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_auto_20180304_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='all_num',
            field=models.IntegerField(verbose_name='\u4e2a\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.IntegerField(verbose_name='\u4ef7\u683c', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_t',
            field=models.DateField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_t',
            field=models.DateField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', blank=True),
        ),
    ]
