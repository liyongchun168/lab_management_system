# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User,Group,Permission
import django.utils.timezone as timezone
from django.db import IntegrityError






class Good(models.Model):
    '''实验室物品'''
    name = models.CharField(max_length=128)
    add_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    num = models.IntegerField(default=1)
    shi_yong_qing_kuang = models.CharField(max_length=128,default=u'无')
    jie = models.CharField(max_length=128,default=u'无')#借给他人
    ke_yong = models.BooleanField(default=True)#借给他人？是否能用
    class Meta:
        ordering= ['-add_date']

    def __unicode__(self):
        return self.name

class ProjectTeam(models.Model):
    '''项目团队'''
    name = models.CharField(max_length=128)
    introduction = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='join_project')#反查参加的项目
    mem_status = models.BooleanField(default=True)#是否可以继续添加人员
    pro_status = models.BooleanField(default=False)#项目是否完成
    plan = models.IntegerField(default=0) #进度
    date = models.DateTimeField(auto_now_add=True)
    leader = models.ForeignKey(User, related_name='lead_project')#项目负责人,反查负责的项目
    show = models.BooleanField(default=True)#是否显示，删除直接讲这个字段改为false

    class Meta:
        ordering = ['-date']

    @property
    def member_num(self):
        return self.members.count() #返回团队的总人数

    @property
    def teachers(self):
        labmembers = self.members.all()
        return [labmember for labmember in labmembers if labmember.is_teacher == True]

    @property
    def students(self):
        labmembers = self.members.all()
        return [labmember for labmember in labmembers if labmember.is_student == True]

    @property
    def money(self):
        finds = self.findingapplication_set.all()
        return sum([find.num for find in finds])

    def __unicode__(self):
        return self.name


class FindingApplication(models.Model):
    '''资金申请'''
    project_team = models.ForeignKey(ProjectTeam)#申请资金的项目团队
    purpose = models.CharField(max_length=200)#申请目的
    status = models.BooleanField(default=False)#申请状态
    num = models.IntegerField(default=0)#数额

    def __unicode__(self):
        return self.project_team

class notice(models.Model):
    '''通知'''
    labmember =models.ForeignKey(User)
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __unicode__(self):
        return self.title

class MessageBoard(models.Model):
    '''留言板'''
    sender = models.ForeignKey(User, related_name='send_msgs')#这两个记好了，这是用来反查用的
    receiver = models.OneToOneField(User, related_name='receive_msgs')
    reply_to = models.ForeignKey('self')#回复的留言
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)#自动添加时间editable=false,blank=true

    def __unicode__(self):
        return '<MossageBoard:%s->%s>'%(self.sender,self.receiver)