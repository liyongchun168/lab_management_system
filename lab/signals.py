# encoding: utf-8

from django.db.models.signals import post_save,post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import User
from django.core.exceptions import ObjectDoesNotExist

# def add_admin(instance):
#     attempts = 0
#     success = False
#     while attempts < 2 and not success:
#         try:
#             a = Group.objects.get(name='admin')
#             instance.groups.add(a)
#             instance.save()
#             success = True
#         except ObjectDoesNotExist:
#             Group.objects.create(name='admin').save()
#
# def add_teacher(instance):
#     attempts = 0
#     success = False
#     while attempts < 2 and not success:
#         try:
#             t = Group.objects.get(name='teacher')
#             instance.groups.add(t)
#             instance.save()
#             success = True
#         except ObjectDoesNotExist:
#             Group.objects.create(name='teacher').save()
#
# def add_student(instance):
#     attempts = 0
#     success = False
#     while attempts < 2 and not success:
#         try:
#             s = Group.objects.get(name='student')
#             instance.groups.add(s)
#             instance.save()
#             success = True
#         except ObjectDoesNotExist:
#             Group.objects.create(name='student').save()

@receiver(post_save, sender=User)
def add_groups(sender, instance,created, **kwargs):
    # if created:
    #
    #     if instance.role==0:
    #         add_admin(instance)
    #
    #     if instance.role==1:
    #         add_teacher(instance)
    #
    #     if instance.role==2:
    #         add_student(instance)
    t = Group.objects.filter(name='teacher').first()
    s = Group.objects.filter(name='student').first()
    p = Group.objects.filter(name='person').first()
    if instance.role==1:
        instance.groups.add(t,p)
    else:
        instance.groups.add(s,p)

@receiver(post_migrate)
def creat_permissions(sender,**kwargs):
    from django.contrib.auth.models import Permission,Group
    from django.contrib.contenttypes.models import ContentType
    from .models import User
    s,created = Group.objects.get_or_create(name='student')
    s.permissions.clear()
    t,created = Group.objects.get_or_create(name='teacher')
    t.permissions.clear()
    p,created = Group.objects.get_or_create(name='person')
    p.permissions.clear()
    # apply_project = Permission.objects.filter(codename='apply_project').first()
    # apply_good = Permission.objects.filter(codename='apply_good').first()
    # apply_finding = Permission.objects.filter(codename='apply_finding').first()
    applys = Permission.objects.filter(codename__startswith='apply')
    # add_good = Permission.objects.filter(codename = 'add_good').first()
    for perm in applys:
        p.permissions.add(perm)#所有人都可以申请物品项目，资金
