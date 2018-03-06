#!/usr/bin/env python
# encoding: utf-8
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import RegexValidator
from .models import Good,Project,User,ProApprove,GoodBorrow
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

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
        fields = ('name','price','all_num')
        # labels = {
        #     'name':_(u'name'),
        #     'price':_(u'price'),
        #     'num':_(u'num'),
        # }

class GoodEditForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('name','price','all_num')

# class GoodBorrowForm(forms.ModelForm):
#
#     def __init__(self,*args,**kwargs):
#         self.user_id = kwargs.pop('user_id',None)
#         self.good_id = kwargs.pop('good_id',None)
#         super(GoodBorrowForm,self).__init__(*args,**kwargs)
#         self.fields['user'].queryset = User.objects.filter(id=self.user_id)
#         self.fields['good'].queryset = Good.objects.filter(id=self.good_id)
#
#     class Meta:
#         model = GoodBorrow
#         fields = ('good','user','num','start_t','end_t')
#
#     def clean(self):
#         good = Good.objects.filter(id = self.good_id).first()
#         if good.active_num<self.num:
#             raise ValidationError(u"你的物品不够了")
#
#     def save_it(self,good,user):
#         g = self.save()
#         g.good = good
#         g.user = user
#         g.save()
#         return g

class GoodBorrowForm(forms.Form):
    num = forms.IntegerField(label=u'数量')
    start_t = forms.DateField(label=u'开始时间')
    end_t = forms.DateField(label=u'结束时间')

    def clean(self):
        cleaned_data = self.cleaned_data
        st = cleaned_data.get('start_t')
        et = cleaned_data.get('end_t')
        if st and et:#必须有这句，因为st或et可能为空
            if st>et:
                raise ValidationError(u'开始时间必须比结束时间早')
        return cleaned_data

class ProjectPulishForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','introduction','start_t','end_t')

    def save_it(self, u):
        p = self.save()#这个必须要先创建，不然在多对多关联的时候没有对象报错
        u.lead_project.add(p)#讲这个用户这位leader
        ProApprove.objects.create(project=p,user=u,status=1)
        # delete_prem = Permission.objects.filter(codename='delete_project').first()
        # try:
        #     apply_premission = Permission.objects.filter(codename='apply_project').first()
        # except ObjectDoesNotExist:
        #     content_type = ContentType.objects.get_for_model(Project)
        #     apply_premission = Permission.objects.create(codename='apply_project',name=u'可以申请项目',content_type=content_type)
        # u.user_premissions.add(apply_premission,delete_premission)#给项目发起人
        # u.user_permissions.add(delete_prem)
        return p