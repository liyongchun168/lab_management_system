
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import User
from django.core.exceptions import ObjectDoesNotExist

def add_admin(instance):
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            a = Group.objects.get(name='admin')
            instance.groups.add(a)
            instance.save()
            success = True
        except ObjectDoesNotExist:
            Group.objects.create(name='admin').save()

def add_teacher(instance):
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            t = Group.objects.get(name='teacher')
            instance.groups.add(t)
            instance.save()
            success = True
        except ObjectDoesNotExist:
            Group.objects.create(name='teacher').save()

def add_student(instance):
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            s = Group.objects.get(name='student')
            instance.groups.add(s)
            instance.save()
            success = True
        except ObjectDoesNotExist:
            Group.objects.create(name='student').save()

@receiver(post_save, sender=User)
def add_groups(sender, instance,created, **kwargs):
    if created:

        if instance.role==0:
            add_admin(instance)

        if instance.role==1:
            add_teacher(instance)

        if instance.role==2:
            add_student(instance)