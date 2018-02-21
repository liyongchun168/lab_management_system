# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0009_auto_20180221_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
