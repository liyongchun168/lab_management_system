# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_auto_20180303_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['-date'], 'permissions': (('apply_good', '\u53ef\u4ee5\u7533\u8bf7\u7269\u54c1'),)},
        ),
        migrations.RenameField(
            model_name='good',
            old_name='add_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='ke_yong',
            new_name='is_active',
        ),
        migrations.RemoveField(
            model_name='good',
            name='jie',
        ),
        migrations.RemoveField(
            model_name='good',
            name='shi_yong_qing_kuang',
        ),
        migrations.AddField(
            model_name='good',
            name='borrow',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='use',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='num',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
