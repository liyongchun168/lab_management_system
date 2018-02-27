# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_auto_20180227_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectteam',
            name='introduction',
            field=models.TextField(verbose_name='\u9879\u76ee\u4ecb\u7ecd', blank=True),
        ),
        migrations.AlterField(
            model_name='projectteam',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u9879\u76ee\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='projectteam',
            name='users',
            field=models.ManyToManyField(related_name='join_project', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
