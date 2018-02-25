# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0010_auto_20180225_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmember',
            name='name',
            field=models.CharField(max_length=7),
        ),
    ]
