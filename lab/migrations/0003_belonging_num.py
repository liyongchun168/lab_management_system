# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20180218_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='belonging',
            name='num',
            field=models.IntegerField(default=1),
        ),
    ]
