# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User,Group,Permission
import django.utils.timezone as timezone
from django.db import IntegrityError

class LabMember(models.Model):
    '''实验室成员'''
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    institute = models.CharField(default=u'信息与计算机学院',max_length=128)

    @staticmethod
    def creat_group():
        try:
            teacher_group = Group.objects.create(name='teacher')
            teacher_group.save()
        except IntegrityError:
            pass
        try:
            student_group = Group.objects.create(name='student')
            student_group.save()
        except IntegrityError:
            pass
        try:
            admin_group = Group.objects.create(name='admin')
            admin_group.save()
        except IntegrityError:
            pass
    @staticmethod
    def assign_permissions():
        permissions = Permission.objects.filter(codename__endswith='good')
        teachers = Group.objects.get(name='teacher')
        for p in permissions:
            teachers.permissions.add(p)
            teachers.save()

    @property
    def teacher(self):
        # 是否是老师，如果不是则为学生,默认为学生
        group = self.user.groups.first()
        if group.name == 'teacher':
            return False
        return True

    def __uncode__(self):
        return self.name

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
    members = models.ManyToManyField(LabMember)

    @property
    def teachers(self):
        labmembers = self.members.all()
        return [labmember for labmember in labmembers if labmember.teacher==True]

    @property
    def students(self):
        labmembers = self.members.all()
        return [labmember for labmember in labmembers if labmember.teacher==False]

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
    labmember =models.ForeignKey(LabMember)
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __unicode__(self):
        return self.title

class MessageBoard(models.Model):
    '''留言板'''
    sender = models.ForeignKey(LabMember,related_name='send_msgs')#这两个记好了，这是用来反查用的
    receiver = models.OneToOneField(LabMember,related_name='receive_msgs')
    reply_to = models.ForeignKey('self')#回复的留言
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)#自动添加时间editable=false,blank=true

    def __unicode__(self):
        return '<MossageBoard:%s->%s>'%(self.sender,self.receiver)