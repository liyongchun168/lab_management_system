#!/usr/bin/env python
# encoding: utf-8
from django import forms
from django.core.validators import RegexValidator
from .models import Good,ProjectTeam,User
# from lab_admin_system.settings import AUTH_USER_MODEL as User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('std_id','password')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','phone','grade','institute','major','adress')

class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('std_id','name')
    def save(self, commit=True):


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

