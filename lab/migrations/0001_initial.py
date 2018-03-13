# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lab.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('std_id', models.CharField(error_messages={b'unique': '\u8be5\u7528\u6237\u5df2\u5b58\u5728'}, max_length=30, validators=[django.core.validators.RegexValidator(b'\\d{1,10}', '\u8bf7\u8f93\u5165\u4e00\u4e2a\u6574\u6570', b'invalid')], help_text='\u8bf7\u8f93\u5165\u5c0f\u4e8e\u5341\u4f4d\u7684\u6570\u5b57', unique=True, verbose_name='\u5b66\u53f7')),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d', blank=True)),
                ('role', models.IntegerField(blank=True, null=True, verbose_name='\u89d2\u8272', choices=[(2, '\u5b66\u751f'), (1, '\u8001\u5e08')])),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=20, verbose_name='\u7535\u8bdd', blank=True)),
                ('grade', models.CharField(blank=True, max_length=4, verbose_name='\u5e74\u7ea7', choices=[(b'2014', '14\u7ea7'), (b'2015', '15\u7ea7'), (b'2016', '16\u7ea7'), (b'2017', '17\u7ea7')])),
                ('institute', models.CharField(default='\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', max_length=30, verbose_name='\u5b66\u9662', choices=[('\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', '\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662'), ('\u56ed\u827a\u5b66\u9662', '\u56ed\u827a\u5b66\u9662'), ('\u5de5\u5b66\u9662', '\u5de5\u5b66\u9662'), ('\u6797\u5b66\u4e0e\u56ed\u6797\u5b66\u9662', '\u6797\u5b66\u4e0e\u56ed\u6797\u5b66\u9662'), ('\u7ecf\u6d4e\u7ba1\u7406\u5b66\u9662', '\u7ecf\u6d4e\u7ba1\u7406\u5b66\u9662'), ('\u519c\u5b66\u9662', '\u519c\u5b66\u9662'), ('\u8336\u4e0e\u98df\u54c1\u79d1\u6280\u5b66\u9662', '\u8336\u4e0e\u98df\u54c1\u79d1\u6280\u5b66\u9662'), ('\u9a6c\u514b\u601d\u4e3b\u4e49\u5b66\u9662', '\u9a6c\u514b\u601d\u4e3b\u4e49\u5b66\u9662'), ('\u7406\u5b66\u9662', '\u7406\u5b66\u9662'), ('\u52a8\u7269\u79d1\u6280\u5b66\u9662', '\u52a8\u7269\u79d1\u6280\u5b66\u9662'), ('\u5916\u56fd\u8bed\u5b66\u9662', '\u5916\u56fd\u8bed\u5b66\u9662'), ('\u8d44\u6e90\u4e0e\u73af\u5883\u5b66\u9662', '\u8d44\u6e90\u4e0e\u73af\u5883\u5b66\u9662'), ('\u8f7b\u7eba\u5de5\u7a0b\u4e0e\u827a\u672f\u5b66\u9662', '\u8f7b\u7eba\u5de5\u7a0b\u4e0e\u827a\u672f\u5b66\u9662'), ('\u4eba\u6587\u793e\u4f1a\u79d1\u5b66\u5b66\u9662', '\u4eba\u6587\u793e\u4f1a\u79d1\u5b66\u5b66\u9662'), ('\u751f\u547d\u79d1\u5b66\u5b66\u9662', '\u751f\u547d\u79d1\u5b66\u5b66\u9662'), ('\u690d\u7269\u4fdd\u62a4\u5b66\u9662', '\u690d\u7269\u4fdd\u62a4\u5b66\u9662')])),
                ('major', models.CharField(max_length=20, verbose_name='\u4e13\u4e1a', blank=True)),
                ('adress', models.CharField(max_length=32, verbose_name='\u4f4f\u5740', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', lab.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purpose', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('num', models.IntegerField(default=0)),
            ],
            options={
                'permissions': (('apply_finding', '\u53ef\u4ee5\u7533\u8bf7\u8d44\u91d1'),),
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u540d\u79f0')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('price', models.IntegerField(verbose_name='\u4ef7\u683c', blank=True)),
                ('all_num', models.IntegerField(verbose_name='\u4e2a\u6570', blank=True)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': '\u7269\u54c1',
                'verbose_name_plural': '\u7269\u54c1',
                'permissions': (('apply_good', '\u53ef\u4ee5\u7533\u8bf7\u7269\u54c1'),),
            },
        ),
        migrations.CreateModel(
            name='GoodBorrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(default=1, verbose_name='\u6570\u91cf')),
                ('start_t', models.DateField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('end_t', models.DateField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('status', models.IntegerField(default=2, choices=[(0, '\u4e0d\u901a\u8fc7'), (1, '\u901a\u8fc7'), (2, '\u7b49\u5f85')])),
                ('good', models.ForeignKey(blank=True, to='lab.Good', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': [],
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
            name='ProApprove',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=2, choices=[(0, '\u4e0d\u901a\u8fc7'), (1, '\u901a\u8fc7'), (2, '\u7b49\u5f85')])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('introduction', models.TextField(verbose_name='\u9879\u76ee\u4ecb\u7ecd', blank=True)),
                ('is_full', models.BooleanField(default=False)),
                ('is_finish', models.BooleanField(default=False)),
                ('plan', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('start_t', models.DateField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('end_t', models.DateField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('leader', models.ForeignKey(related_name='lead_project', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='lab.ProApprove', blank=True)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': '\u9879\u76ee',
                'verbose_name_plural': '\u9879\u76ee',
                'permissions': (('apply_project', '\u53ef\u4ee5\u7533\u8bf7\u9879\u76ee'),),
            },
        ),
        migrations.AddField(
            model_name='proapprove',
            name='project',
            field=models.ForeignKey(blank=True, to='lab.Project', null=True),
        ),
        migrations.AddField(
            model_name='proapprove',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='good',
            name='user_borrowed',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='lab.GoodBorrow', blank=True),
        ),
        migrations.AddField(
            model_name='finding',
            name='project',
            field=models.ForeignKey(to='lab.Project'),
        ),
    ]
