# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab', '0006_auto_20180220_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindingApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purpose', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LabMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('institute', models.CharField(default='\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', max_length=128)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('introduction', models.TextField(blank=True)),
                ('members', models.ManyToManyField(to='lab.LabMember')),
            ],
        ),
        migrations.DeleteModel(
            name='Money',
        ),
        migrations.RemoveField(
            model_name='schooluser',
            name='school_user',
        ),
        migrations.DeleteModel(
            name='SchoolUser',
        ),
        migrations.AddField(
            model_name='findingapplication',
            name='project_team',
            field=models.ForeignKey(to='lab.ProjectTeam'),
        ),
    ]
