# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labmember',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='labmember',
            name='image',
            field=models.ImageField(max_length=120, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='labmember',
            name='phone',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
