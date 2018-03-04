# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_auto_20180304_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodBorrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('returned', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['-date'], 'verbose_name': '\u7269\u54c1', 'verbose_name_plural': '\u7269\u54c1', 'permissions': (('apply_good', '\u53ef\u4ee5\u7533\u8bf7\u7269\u54c1'),)},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date'], 'verbose_name': '\u9879\u76ee', 'verbose_name_plural': '\u9879\u76ee', 'permissions': (('apply_project', '\u53ef\u4ee5\u7533\u8bf7\u9879\u76ee'),)},
        ),
        migrations.RenameField(
            model_name='good',
            old_name='num',
            new_name='all_num',
        ),
        migrations.RemoveField(
            model_name='good',
            name='borrow',
        ),
        migrations.RemoveField(
            model_name='good',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='good',
            name='use',
        ),
        migrations.AddField(
            model_name='goodborrow',
            name='good',
            field=models.ForeignKey(to='lab.Good'),
        ),
        migrations.AddField(
            model_name='goodborrow',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='good',
            name='user_borrowed',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, through='lab.GoodBorrow', blank=True),
        ),
    ]
