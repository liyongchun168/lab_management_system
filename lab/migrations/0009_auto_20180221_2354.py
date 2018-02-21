# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_notice_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver', models.OneToOneField(related_name='receive_msgs', to='lab.LabMember')),
                ('reply_to', models.ForeignKey(to='lab.MessageBoard')),
                ('sender', models.ForeignKey(related_name='send_msgs', to='lab.LabMember')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
