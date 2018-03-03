#!/usr/bin/env python
# encoding: utf-8
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import RegexValidator
from .models import Good,Project,User,ProApprove
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class LoginForm(forms.Form):
    std_id = forms.CharField(max_length=30)
    password = forms.CharField(max_length=128,widget=forms.PasswordInput)

# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email','phone','grade','institute','major','adress')

# class UserAddForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('std_id','name','role')
#
#     def save(self, commit=True):
#         # 密码默认为学号
#         user = super(UserAddForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["std_id"])
#         if commit:
#             user.save()
#         return user

class GoodAddForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('name','price','num')
        # labels = {
        #     'name':_(u'name'),
        #     'price':_(u'price'),
        #     'num':_(u'num'),
        # }

class GoodEditForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('name','price','num','shi_yong_qing_kuang','jie')

class ProjectPulishForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','introduction')

    def save_it(self, u):
        p = self.save()#这个必须要先创建，不然在多对多关联的时候没有对象报错
        u.lead_project.add(p)#讲这个用户这位leader
        ProApprove.objects.create(project=p,user=u,status=2)
        # delete_prem = Permission.objects.filter(codename='delete_project').first()
        # try:
        #     apply_premission = Permission.objects.filter(codename='apply_project').first()
        # except ObjectDoesNotExist:
        #     content_type = ContentType.objects.get_for_model(Project)
        #     apply_premission = Permission.objects.create(codename='apply_project',name=u'可以申请项目',content_type=content_type)
        # u.user_premissions.add(apply_premission,delete_premission)#给项目发起人
        # u.user_permissions.add(delete_prem)
        return p