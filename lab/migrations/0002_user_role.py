# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(default=1, choices=[(2, '\u5b66\u751f'), (1, '\u8001\u5e08')]),
            preserve_default=False,
        ),
    ]
