# encoding: utf-8
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

    def create_superuser(self, std_id, email, password, **extra_fields):
        return self._create_user(std_id, email, password, True, True,
                                 **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    grade_list = (#为grade提供选项
        ('2014',u'14级'),
        ('2015',u'15级'),
        ('2016',u'16级'),
        ('2017',u'17级'),
    )

    std_id = models.CharField(_('student number'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'\d{1,30}',
                                      u'请输入一个整数', 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that std_id already exists."),
        })
    name = models.CharField(_('name'), max_length=30)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    phone = models.CharField(blank=True,max_length=20)
    # image = models.ImageField(blank=True,max_length=120)#用户头像
    grade = models.CharField(blank=True,max_length=4,choices=grade_list)
    institute = models.CharField(default=u'信息与计算机学院',max_length=128)
    major = models.CharField(blank=True,max_length=20)#专业
    adress = models.CharField(blank=True,max_length=32)#住址
    objects = UserManager()

    USERNAME_FIELD = 'std_id'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


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
#     role_list = {
#         (1,u'老师'),
#         (2,u'学生'),
#
#     }
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

