# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20180227_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purpose', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='findingapplication',
            name='project_team',
        ),
        migrations.RenameField(
            model_name='projectteam',
            old_name='show',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='projectteam',
            old_name='members',
            new_name='users',
        ),
        migrations.AlterField(
            model_name='user',
            name='institute',
            field=models.CharField(default='\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', max_length=5, verbose_name='\u5b66\u9662', choices=[('\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', '\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662'), ('\u56ed\u827a\u5b66\u9662', '\u56ed\u827a\u5b66\u9662'), ('\u5de5\u5b66\u9662', '\u5de5\u5b66\u9662'), ('\u6797\u5b66\u4e0e\u56ed\u6797\u5b66\u9662', '\u6797\u5b66\u4e0e\u56ed\u6797\u5b66\u9662'), ('\u7ecf\u6d4e\u7ba1\u7406\u5b66\u9662', '\u7ecf\u6d4e\u7ba1\u7406\u5b66\u9662'), ('\u519c\u5b66\u9662', '\u519c\u5b66\u9662'), ('\u8336\u4e0e\u98df\u54c1\u79d1\u6280\u5b66\u9662', '\u8336\u4e0e\u98df\u54c1\u79d1\u6280\u5b66\u9662'), ('\u9a6c\u514b\u601d\u4e3b\u4e49\u5b66\u9662', '\u9a6c\u514b\u601d\u4e3b\u4e49\u5b66\u9662'), ('\u7406\u5b66\u9662', '\u7406\u5b66\u9662'), ('\u52a8\u7269\u79d1\u6280\u5b66\u9662', '\u52a8\u7269\u79d1\u6280\u5b66\u9662'), ('\u5916\u56fd\u8bed\u5b66\u9662', '\u5916\u56fd\u8bed\u5b66\u9662'), ('\u8d44\u6e90\u4e0e\u73af\u5883\u5b66\u9662', '\u8d44\u6e90\u4e0e\u73af\u5883\u5b66\u9662'), ('\u8f7b\u7eba\u5de5\u7a0b\u4e0e\u827a\u672f\u5b66\u9662', '\u8f7b\u7eba\u5de5\u7a0b\u4e0e\u827a\u672f\u5b66\u9662'), ('\u4eba\u6587\u793e\u4f1a\u79d1\u5b66\u5b66\u9662', '\u4eba\u6587\u793e\u4f1a\u79d1\u5b66\u5b66\u9662'), ('\u751f\u547d\u79d1\u5b66\u5b66\u9662', '\u751f\u547d\u79d1\u5b66\u5b66\u9662'), ('\u690d\u7269\u4fdd\u62a4\u5b66\u9662', '\u690d\u7269\u4fdd\u62a4\u5b66\u9662')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='std_id',
            field=models.CharField(error_messages={b'unique': '\u8be5\u7528\u6237\u5df2\u5b58\u5728'}, max_length=10, validators=[django.core.validators.RegexValidator(b'\\d{1,10}', '\u8bf7\u8f93\u5165\u4e00\u4e2a\u6574\u6570', b'invalid')], help_text='\u8bf7\u8f93\u5165\u5c0f\u4e8e\u5341\u4f4d\u7684\u6570\u5b57', unique=True, verbose_name='\u5b66\u53f7'),
        ),
        migrations.DeleteModel(
            name='FindingApplication',
        ),
        migrations.AddField(
            model_name='finding',
            name='project_team',
            field=models.ForeignKey(to='lab.ProjectTeam'),
        ),
    ]
