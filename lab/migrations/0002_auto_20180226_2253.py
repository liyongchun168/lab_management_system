# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectteam',
            name='leader',
            field=models.ForeignKey(related_name='lead_project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectteam',
            name='members',
            field=models.ManyToManyField(related_name='join_project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notice',
            name='labmember',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='receiver',
            field=models.OneToOneField(related_name='receive_msgs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='reply_to',
            field=models.ForeignKey(to='lab.MessageBoard'),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='sender',
            field=models.ForeignKey(related_name='send_msgs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='findingapplication',
            name='project_team',
            field=models.ForeignKey(to='lab.ProjectTeam'),
        ),
    ]
