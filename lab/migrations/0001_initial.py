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
                ('std_id', models.CharField(error_messages={b'unique': 'A user with that std_id already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'\\d{1,30}', '\u8bf7\u8f93\u5165\u4e00\u4e2a\u6574\u6570', b'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='student number')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('grade', models.CharField(blank=True, max_length=4, choices=[(b'2014', '14\u7ea7'), (b'2015', '15\u7ea7'), (b'2016', '16\u7ea7'), (b'2017', '17\u7ea7')])),
                ('institute', models.CharField(default='\u4fe1\u606f\u4e0e\u8ba1\u7b97\u673a\u5b66\u9662', max_length=128)),
                ('major', models.CharField(max_length=20, blank=True)),
                ('adress', models.CharField(max_length=32, blank=True)),
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
