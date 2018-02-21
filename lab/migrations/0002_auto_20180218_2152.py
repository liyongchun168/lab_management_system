# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belonging',
            name='jie',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='belonging',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='belonging',
            name='shi_yong_qing_kuang',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
