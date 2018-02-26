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
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.OneToOneField(related_name='receive_msgs', to=settings.AUTH_USER_MODEL)),
                ('reply_to', models.ForeignKey(to='lab.MessageBoard')),
                ('sender', models.ForeignKey(related_name='send_msgs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('labmember', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.IntegerField(choices=[(2, '\u5b66\u751f'), (1, '\u8001\u5e08')])),
                ('name', models.CharField(max_length=7)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('image', models.ImageField(max_length=120, upload_to=b'', blank=True)),
                ('grade', models.CharField(blank=True, max_length=4, choices=[(b'2014', '14\u7ea7'), (b'2015', '15\u7ea7'), (b'2016', '16\u7ea7'), (b'2017', '17\u7ea7')])),
                ('institute', models.CharField(default='\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', max_length=128)),
                ('major', models.CharField(max_length=20, blank=True)),
                ('adress', models.CharField(max_length=32, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
                ('leader', models.ForeignKey(related_name='lead_project', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='join_project', to=settings.AUTH_USER_MODEL)),
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
