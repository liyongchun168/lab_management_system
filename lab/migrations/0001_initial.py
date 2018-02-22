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
            name='FindingApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purpose', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
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
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.OneToOneField(related_name='receive_msgs', to='lab.LabMember')),
                ('reply_to', models.ForeignKey(to='lab.MessageBoard')),
                ('sender', models.ForeignKey(related_name='send_msgs', to='lab.LabMember')),
            ],
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('labmember', models.ForeignKey(to='lab.LabMember')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('introduction', models.TextField(blank=True)),
                ('mem_status', models.BooleanField(default=True)),
                ('pro_status', models.BooleanField(default=False)),
                ('plan', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('show', models.BooleanField(default=True)),
                ('leader', models.ForeignKey(related_name='lead_project', to='lab.LabMember')),
                ('members', models.ManyToManyField(related_name='join_project', to='lab.LabMember')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='findingapplication',
            name='project_team',
            field=models.ForeignKey(to='lab.ProjectTeam'),
        ),
    ]
