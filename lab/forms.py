#!/usr/bin/env python
# encoding: utf-8
from django import forms
from django.core.validators import RegexValidator
from .models import Good,ProjectTeam,User

class LoginForm(forms.Form):
    std_id = forms.CharField(max_length=30)
    password = forms.CharField(max_length=128,widget=forms.PasswordInput)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','phone','grade','institute','major','adress')

class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('std_id','name','role')

    def save(self, commit=True):
        # 密码默认为学号
        user = super(UserAddForm, self).save(commit=False)
        user.set_password(self.cleaned_data["std_id"])
        if commit:
            user.save()
        return user

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
        model = ProjectTeam
        fields = ('name','introduction','leader')

