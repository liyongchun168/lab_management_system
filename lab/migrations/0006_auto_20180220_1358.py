# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_auto_20180219_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=1)),
                ('shi_yong_qing_kuang', models.CharField(default='\u65e0', max_length=128)),
                ('jie', models.CharField(default='\u65e0', max_length=128)),
                ('ke_yong', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-add_date'],
            },
        ),
        migrations.DeleteModel(
            name='Belonging',
        ),
    ]
