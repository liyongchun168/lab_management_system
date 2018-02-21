# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0010_auto_20180222_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
