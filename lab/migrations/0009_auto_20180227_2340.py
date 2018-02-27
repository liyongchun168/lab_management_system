# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_auto_20180227_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectteam',
            name='leader',
            field=models.ForeignKey(related_name='lead_project', default=1, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
