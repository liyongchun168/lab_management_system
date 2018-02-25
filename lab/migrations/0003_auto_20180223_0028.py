# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20180222_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='labmember',
            name='adress',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='labmember',
            name='grade',
            field=models.CharField(blank=True, max_length=4, choices=[(b'2014', b'14\xe7\xba\xa7'), (b'2015', b'15\xe7\xba\xa7'), (b'2016', b'16\xe7\xba\xa7'), (b'2017', b'17\xe7\xba\xa7')]),
        ),
        migrations.AddField(
            model_name='labmember',
            name='major',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
