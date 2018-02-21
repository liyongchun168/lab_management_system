# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20180219_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belonging',
            name='jie',
            field=models.CharField(default='\u65e0', max_length=128),
        ),
        migrations.AlterField(
            model_name='belonging',
            name='shi_yong_qing_kuang',
            field=models.CharField(default='\u65e0', max_length=128),
        ),
    ]
