# encoding: utf-8
from django.contrib.auth.models import Group,Permission
from lab_admin_system import settings
from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractBaseUser, PermissionsMixin
from django.db import IntegrityError
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, std_id, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not std_id:
            raise ValueError('The given std_id must be set')
        email = self.normalize_email(email)
        user = self.model(std_id=std_id, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, std_id, email=None, password=None, **extra_fields):
        return self._create_user(std_id, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, std_id, password,email=None, **extra_fields):
        return self._create_user(std_id, email, password, True, True,
                                 **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    grade_list = (#为grade提供选项
        ('2014',u'14级'),
        ('2015',u'15级'),
        ('2016',u'16级'),
        ('2017',u'17级'),
    )

    role_list = {
        (1, u'老师'),
        (2, u'学生'),
    }

    institute_list = {

        (u'农学院',u'农学院'),
        (u'植物保护学院',u'植物保护学院'),
        (u'园艺学院',u'园艺学院'),
        (u'林学与园林学院',u'林学与园林学院'),
        (u'动物科技学院',u'动物科技学院'),
        (u'茶与食品科技学院',u'茶与食品科技学院'),
        (u'理学院',u'理学院'),
        (u'生命科学学院',u'生命科学学院'),
        (u'资源与环境学院',u'资源与环境学院'),
        (u'工学院',u'工学院'),
        (u'轻纺工程与艺术学院',u'轻纺工程与艺术学院'),
        (u'信息与计算机学院',u'信息与计算机学院'),
        (u'经济管理学院',u'经济管理学院'),
        (u'人文社会科学学院',u'人文社会科学学院'),
        (u'外国语学院',u'外国语学院'),
        (u'马克思主义学院',u'马克思主义学院'),
    }

    std_id = models.CharField(u'学号', max_length=30, unique=True,
        help_text=u'请输入小于十位的数字',
        validators=[
            validators.RegexValidator(r'\d{1,10}',
                                      u'请输入一个整数', 'invalid'),
        ],
        error_messages={
            'unique': u'该用户已存在',
        })
    name = models.CharField(u'姓名', max_length=30,blank=True)
    role = models.IntegerField(u'角色',choices=role_list,blank=True,null=True)  # 角色:老师，学生
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    phone = models.CharField(u'电话',blank=True,max_length=20)
    grade = models.CharField(u'年级',blank=True,max_length=4,choices=grade_list)
    institute = models.CharField(u'学院',default=u'信息与计算机学院',choices=institute_list,max_length=30)
    major = models.CharField('专业',blank=True,max_length=20)#专业
    adress = models.CharField(u'住址',blank=True,max_length=32)#住址
    objects = UserManager()

    USERNAME_FIELD = 'std_id'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        return self.name[1:]

    def get_full_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
#
# class User(AbstractUser):
#     '''实验室成员'''
#
#
    # role_list = {
    #     (1,u'老师'),
    #     (2,u'学生'),
    # }
#
#     # user = models.OneToOneField(User)#OneToOne关系默认使用关联成员的小写，比如这个反查默认user.labmember，我改为lab,以弃用
#     # role = models.IntegerField(choices=role_list)#角色：管理员，老师，学生
#     name = models.CharField(max_length=7,blank=True)
#     email = models.EmailField(blank=True)
#
#
#     @staticmethod
#     def creat_group():
#         try:
#             teacher_group = Group.objects.create(name='teacher')
#             teacher_group.save()
#         except IntegrityError:
#             pass
#         try:
#             student_group = Group.objects.create(name='student')
#             student_group.save()
#         except IntegrityError:
#             pass
#         try:
#             admin_group = Group.objects.create(name='admin')
#             admin_group.save()
#         except IntegrityError:
#             pass
#     @staticmethod
#     def assign_permissions():
#         good_p = Permission.objects.filter(codename__endswith='good')
#         user_p = Permission.objects.filter(codename__endswith='user')
#         admin = Group.objects.get(name='admin')
#         for p in good_p:
#             admin.permissions.add(p)
#             admin.save()
#         for p in user_p:
#             admin.permissions.add(p)
#             admin.save()
#
#     # @property
#     # def is_teacher(self):
#     #     # 是否是老师，如果不是则为学生,默认为学生
#     #     group = self.user.groups.first()
#     #     if group.name == 'teacher' or group.name == 'admin':
#     #         return True
#     #     return False
#     #
#     # @property
#     # def is_student(self):
#     #     group = self.user.groups.first()
#     #     if group.name == 'student':
#     #         return True
#     #     return False
#     #
#     # @property
#     # def is_admin(self):
#     #     group = self.user.groups.first()
#     #     if group.name == 'admin':
#     #         return True
#     #     return False
#
#     def __iter__(self):
#         fields = [self.name,self.email,self.phone,self.grade,self.institute,self.major,self.adress]
#         for i in fields:
#             yield i
#
#     def __unicode__(self):
#         return self.name




class Project(models.Model):
    '''项目团队'''
    name = models.CharField(u'项目名称',max_length=128)
    introduction = models.TextField(u'项目介绍',blank=True)
    users = models.ManyToManyField(User, blank=True,through='ProApprove')#反查参加的项目
    is_full= models.BooleanField(default=False)#人员是否收满了
    is_finish = models.BooleanField(default=False)#项目是否完成了
    plan = models.IntegerField(default=0) #进度
    date = models.DateTimeField(auto_now_add=True)
    leader = models.ForeignKey(User,blank=True,null=True,related_name='lead_project')#项目负责人,反查负责的项目
    is_active = models.BooleanField(default=True)#是否显示，删除直接讲这个字段改为false

    class Meta:
        ordering = ['-date']
        permissions = (
            ("apply_project", u"可以申请项目"),
        )

    @property
    def member_num(self):
        return self.users.count() #返回团队的总人数

    @property
    def teachers(self):
        users = self.users.all()
        return [user for user in users if user.role == 1]

    @property
    def students(self):
        users = self.users.all()
        return [user for user in users if user.role == 2]

    @property
    def money(self):
        finds = self.finding_set.all()
        return sum([find.num for find in finds])

    # def __unicode__(self):
    #     return self.name



class ProApprove(models.Model):
    project = models.ForeignKey(Project,blank=True,null=True)
    user = models.ForeignKey(User)
    status = models.IntegerField(default=2,choices=((0,u'不通过'),(1,u'通过'),(2,u'等待'),))



class Finding(models.Model):
    '''资金申请'''
    project = models.ForeignKey(Project)#申请资金的项目团队
    purpose = models.CharField(max_length=200)#申请目的
    status = models.BooleanField(default=False)#申请状态
    num = models.IntegerField(default=0)#数额

    def __unicode__(self):
        return self.purpose



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

class notice(models.Model):
    '''通知'''
    labmember =models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __unicode__(self):
        return self.title

class MessageBoard(models.Model):
    '''留言板'''
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='send_msgs')#这两个记好了，这是用来反查用的
    receiver = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='receive_msgs')
    reply_to = models.ForeignKey('self')#回复的留言
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)#自动添加时间editable=false,blank=true

    def __unicode__(self):
        return '<MossageBoard:%s->%s>'%(self.sender,self.receiver)