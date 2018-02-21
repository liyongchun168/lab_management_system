# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Belonging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
                ('shi_yong_qing_kuang', models.CharField(max_length=128)),
                ('jie', models.CharField(max_length=128)),
                ('ke_yong', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('use', models.CharField(max_length=128)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=128)),
                ('school_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
