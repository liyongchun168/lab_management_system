# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_belonging_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='belonging',
            options={'ordering': ['-add_date']},
        ),
        migrations.AddField(
            model_name='belonging',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
