# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User,Group,Permission
from django.db import IntegrityError

class Profile(models.Model):
    '''实验室成员'''
    grade_list = (#为grade提供选项
        ('2014',u'14级'),
        ('2015',u'15级'),
        ('2016',u'16级'),
        ('2017',u'17级'),
    )

    role_list = {
        (1,u'老师'),
        (2,u'学生'),

    }

    user = models.OneToOneField(User)#OneToOne关系默认使用关联成员的小写，比如这个反查默认user.labmember，我改为lab,以弃用
    # role = models.IntegerField(choices=role_list)#角色：管理员，老师，学生
    name = models.CharField(max_length=7,blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True,max_length=20)
    image = models.ImageField(blank=True,max_length=120)#用户头像
    grade = models.CharField(blank=True,max_length=4,choices=grade_list)
    institute = models.CharField(default=u'信息与计算机学院',max_length=128)
    major = models.CharField(blank=True,max_length=20)#专业
    adress = models.CharField(blank=True,max_length=32)#住址
    date = models.DateTimeField(auto_now_add=True)

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
        good_p = Permission.objects.filter(codename__endswith='good')
        user_p = Permission.objects.filter(codename__endswith='user')
        admin = Group.objects.get(name='admin')
        for p in good_p:
            admin.permissions.add(p)
            admin.save()
        for p in user_p:
            admin.permissions.add(p)
            admin.save()

    # @property
    # def is_teacher(self):
    #     # 是否是老师，如果不是则为学生,默认为学生
    #     group = self.user.groups.first()
    #     if group.name == 'teacher' or group.name == 'admin':
    #         return True
    #     return False
    #
    # @property
    # def is_student(self):
    #     group = self.user.groups.first()
    #     if group.name == 'student':
    #         return True
    #     return False
    #
    # @property
    # def is_admin(self):
    #     group = self.user.groups.first()
    #     if group.name == 'admin':
    #         return True
    #     return False

    def __iter__(self):
        fields = [self.name,self.email,self.phone,self.grade,self.institute,self.major,self.adress]
        for i in fields:
            yield i

    def __unicode__(self):
        return self.name
