# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_labmember_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='labmember',
            name='role',
            field=models.IntegerField(default=2, choices=[(2, '\u5b66\u751f'), (1, '\u8001\u5e08'), (0, '\u7ba1\u7406\u5458')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='labmember',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
