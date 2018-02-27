# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='std_id',
            field=models.CharField(error_messages={b'unique': 'A user with that std_id already exists.'}, max_length=10, validators=[django.core.validators.RegexValidator(b'\\d{1,10}', '\u8bf7\u8f93\u5165\u4e00\u4e2a\u6574\u6570', b'invalid')], help_text='\u8bf7\u8f93\u5165\u5c0f\u4e0e\u5341\u4f4d\u7684\u6570\u5b57', unique=True, verbose_name='\u5b66\u53f7'),
        ),
    ]
