# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0009_auto_20180304_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodborrow',
            options={'ordering': []},
        ),
        migrations.RemoveField(
            model_name='goodborrow',
            name='created',
        ),
        migrations.RemoveField(
            model_name='goodborrow',
            name='returned',
        ),
        migrations.AddField(
            model_name='goodborrow',
            name='end_t',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='goodborrow',
            name='start_t',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='goodborrow',
            name='good',
            field=models.ForeignKey(blank=True, to='lab.Good', null=True),
        ),
        migrations.AlterField(
            model_name='goodborrow',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
