#!/usr/bin/env python
# encoding: utf-8
from django import forms
from django.core.validators import RegexValidator
from .models import Good,ProjectTeam



from django.utils.translation import ugettext_lazy as _
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

