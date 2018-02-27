# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_auto_20180228_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u89d2\u8272', choices=[(2, '\u5b66\u751f'), (1, '\u8001\u5e08')]),
        ),
    ]
