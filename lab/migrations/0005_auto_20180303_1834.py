# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20180303_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finding',
            options={'permissions': (('apply_finding', '\u53ef\u4ee5\u7533\u8bf7\u8d44\u91d1'),)},
        ),
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['-add_date'], 'permissions': (('apply_good', '\u53ef\u4ee5\u7533\u8bf7\u7269\u54c1'),)},
        ),
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.CharField(max_length=20, verbose_name='\u4e13\u4e1a', blank=True),
        ),
    ]
