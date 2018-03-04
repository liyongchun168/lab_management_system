# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_auto_20180304_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_t',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_t',
            field=models.DateField(null=True, blank=True),
        ),
    ]
