# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_auto_20180223_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmember',
            name='user',
            field=models.OneToOneField(related_name='lab', to=settings.AUTH_USER_MODEL),
        ),
    ]
