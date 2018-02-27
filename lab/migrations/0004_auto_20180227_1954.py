# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_auto_20180227_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='adress',
            field=models.CharField(max_length=32, verbose_name='\u4f4f\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(blank=True, max_length=4, verbose_name='\u5e74\u7ea7', choices=[(b'2014', '14\u7ea7'), (b'2015', '15\u7ea7'), (b'2016', '16\u7ea7'), (b'2017', '17\u7ea7')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='institute',
            field=models.CharField(default=b'x', max_length=5, verbose_name='\u5b66\u9662', choices=[(b'c', '\u8336\u4e0e\u98df\u54c1\u79d1\u6280\u5b66\u9662'), (b'z', '\u8d44\u6e90\u4e0e\u73af\u5883\u5b66\u9662'), (b'n', '\u519c\u5b66\u9662'), (b's', '\u751f\u547d\u79d1\u5b66\u5b66\u9662'), (b'd', '\u52a8\u7269\u79d1\u6280\u5b66\u9662'), (b'j', '\u7ecf\u6d4e\u7ba1\u7406\u5b66\u9662'), (b'm', '\u9a6c\u514b\u601d\u4e3b\u4e49\u5b66\u9662'), (b'li', '\u7406\u5b66\u9662'), (b'r', '\u4eba\u6587\u793e\u4f1a\u79d1\u5b66\u5b66\u9662'), (b'z', '\u690d\u7269\u4fdd\u62a4\u5b66\u9662'), (b'q', '\u8f7b\u7eba\u5de5\u7a0b\u4e0e\u827a\u672f\u5b66\u9662'), (b'x', '\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662'), (b'l', '\u6797\u5b66\u4e0e\u56ed\u6797\u5b66\u9662'), (b'g', '\u5de5\u5b66\u9662'), (b'y', '\u56ed\u827a\u5b66\u9662'), (b'w', '\u5916\u56fd\u8bed\u5b66\u9662')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.CharField(max_length=20, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='\u7535\u8bdd', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(verbose_name='\u89d2\u8272', choices=[(2, '\u5b66\u751f'), (1, '\u8001\u5e08')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='std_id',
            field=models.CharField(error_messages={b'unique': 'A user with that std_id already exists.'}, max_length=10, validators=[django.core.validators.RegexValidator(b'\\d{1,10}', '\u8bf7\u8f93\u5165\u4e00\u4e2a\u6574\u6570', b'invalid')], help_text='\u8bf7\u8f93\u5165\u5c0f\u4e8e\u5341\u4f4d\u7684\u6570\u5b57', unique=True, verbose_name='\u5b66\u53f7'),
        ),
    ]
