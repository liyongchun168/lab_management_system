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
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('role', models.IntegerField(verbose_name='\u89d2\u8272', choices=[(2, '\u5b66\u751f'), (1, '\u8001\u5e08')])),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=20, verbose_name='\u7535\u8bdd', blank=True)),
                ('grade', models.CharField(blank=True, max_length=4, verbose_name='\u5e74\u7ea7', choices=[(b'2014', '14\u7ea7'), (b'2015', '15\u7ea7'), (b'2016', '16\u7ea7'), (b'2017', '17\u7ea7')])),
                ('institute', models.CharField(default='\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', max_length=5, verbose_name='\u5b66\u9662', choices=[('\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', '\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662'), ('\u56ed\u827a\u5b66\u9662', '\u56ed\u827a\u5b66\u9662'), ('\u5de5\u5b66\u9662', '\u5de5\u5b66\u9662'), ('\u6797\u5b66\u4e0e\u56ed\u6797\u5b66\u9662', '\u6797\u5b66\u4e0e\u56ed\u6797\u5b66\u9662'), ('\u7ecf\u6d4e\u7ba1\u7406\u5b66\u9662', '\u7ecf\u6d4e\u7ba1\u7406\u5b66\u9662'), ('\u519c\u5b66\u9662', '\u519c\u5b66\u9662'), ('\u8336\u4e0e\u98df\u54c1\u79d1\u6280\u5b66\u9662', '\u8336\u4e0e\u98df\u54c1\u79d1\u6280\u5b66\u9662'), ('\u9a6c\u514b\u601d\u4e3b\u4e49\u5b66\u9662', '\u9a6c\u514b\u601d\u4e3b\u4e49\u5b66\u9662'), ('\u7406\u5b66\u9662', '\u7406\u5b66\u9662'), ('\u52a8\u7269\u79d1\u6280\u5b66\u9662', '\u52a8\u7269\u79d1\u6280\u5b66\u9662'), ('\u5916\u56fd\u8bed\u5b66\u9662', '\u5916\u56fd\u8bed\u5b66\u9662'), ('\u8d44\u6e90\u4e0e\u73af\u5883\u5b66\u9662', '\u8d44\u6e90\u4e0e\u73af\u5883\u5b66\u9662'), ('\u8f7b\u7eba\u5de5\u7a0b\u4e0e\u827a\u672f\u5b66\u9662', '\u8f7b\u7eba\u5de5\u7a0b\u4e0e\u827a\u672f\u5b66\u9662'), ('\u4eba\u6587\u793e\u4f1a\u79d1\u5b66\u5b66\u9662', '\u4eba\u6587\u793e\u4f1a\u79d1\u5b66\u5b66\u9662'), ('\u751f\u547d\u79d1\u5b66\u5b66\u9662', '\u751f\u547d\u79d1\u5b66\u5b66\u9662'), ('\u690d\u7269\u4fdd\u62a4\u5b66\u9662', '\u690d\u7269\u4fdd\u62a4\u5b66\u9662')])),
                ('major', models.CharField(max_length=20, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a', blank=True)),
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
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('introduction', models.TextField(verbose_name='\u9879\u76ee\u4ecb\u7ecd', blank=True)),
                ('mem_status', models.BooleanField(default=True)),
                ('pro_status', models.BooleanField(default=False)),
                ('plan', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('leader', models.ForeignKey(related_name='lead_project', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('users', models.ManyToManyField(related_name='join_project', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='finding',
            name='project_team',
            field=models.ForeignKey(to='lab.Project'),
        ),
    ]
