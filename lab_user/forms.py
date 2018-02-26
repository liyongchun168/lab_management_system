# encoding:utf-8
from django import forms
from django.core.validators import RegexValidator
from .models import Profile

class Login_form(forms.Form):
    name = forms.CharField(label=u'学号',max_length=128,validators=[RegexValidator(regex='\d{1,30}',message=u'请输入正确的格式')])
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput)

class Register_form(forms.Form):
    group_list = (
        ('teacher',u'老师'),
        ('student',u'学生'),
    )
    name = forms.CharField(label=u'学号',max_length=128,validators=[RegexValidator(regex='\d{1,30}',message=u'请输入正确的格式')])
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput)
    user_group  = forms.ChoiceField(choices=group_list)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','name','email','phone','grade','institute','major','adress']

class UserAddForm(forms.Form):
    # user = forms.CharField(max_length=128,validators=[RegexValidator(regex='\d{1,30}',message=u'请输入正确的格式')])
    # class Meta:
    #     model = LabMember
    #     fields = ['image','name','email','phone','grade','institute','major','adress']

    role_list = {
        (1,u'老师'),
        (2,u'学生'),
    }

    school_num = forms.CharField(label=u'学号',max_length=128, validators=[RegexValidator(regex='\d{1,30}', message=u'请输入正确的格式')])
    name = forms.CharField(label=u'姓名',max_length=7)
    role = forms.TypedChoiceField(label=u'角色',choices=role_list,coerce=int)