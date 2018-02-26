# encoding:utf-8
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required,login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseNotFound
from django.core.urlresolvers import reverse
from .forms import Login_form,Register_form,UserEditForm,UserAddForm
from django.contrib.auth.models import User,Group,Permission

# 用户模块

def login_view(request):
    error_msg = ""
    if request.method=='POST':

        login_form = Login_form(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['name']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                error_msg = u'用户名和密码不匹配'
        else:
            error_msg = u'请检查你的输入格式是否正确'
    else:
        login_form = Login_form()
    return render(request,'registration/login.html',{'login_form':login_form,'error_msg':error_msg})
# def register(request):
#     error_msg = ''
#     if request.method=='POST':
#         try:
#             LabMember.creat_group()
#         except IntegrityError:
#             pass
#         register_form = Register_form(request.POST)
#         if register_form.is_valid():
#             username = register_form.cleaned_data['name']
#             password = register_form.cleaned_data['password']
#             user_group = register_form.cleaned_data['user_group']
#             try:
#                 user = User.objects.create_user(username=username,password=password)
#                 user.save()
#                 try:
#                     group = Group.objects.get(name=user_group)
#                     user.groups.add(group)
#                     user.save()
#                     return HttpResponseRedirect(reverse('login'))
#                 except Exception:
#                     error_msg = u'用户角色设置错误'
#             except IntegrityError:
#                 error_msg = u'该账号已被注册'
#             except Exception:
#                 error_msg = u'出现内部错误,请稍后再试'
#     else:
#         register_form = Register_form()
#     return render(request,'registration/register.html',{'register_form':register_form,'error_msg':error_msg})

@login_required
def user_view(request,user_id):
    try:
        lab_user = Profile.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('404')
    return render(request,'user_page.html', {'lab_user':lab_user})

@login_required
def user_edit(request):
    #
    # try:
    #     user = LabMember.objects.get(id=user_id)
    # except ObjectDoesNotExist:
    #     return HttpResponseNotFound('404')
    # if request.user.lab.id != user.id:#如果修改的用户不是当前用户就返回404
    #     return HttpResponseNotFound('404没有找到')
    # if request.method == 'POST':
    #     user_form = UserEditForm(request.POST,instance=user)
    #     if user_form.is_valid():
    #         user_form.save()
    #         return HttpResponseRedirect(reverse('user_view',args=(user_id,)))
    # else:
    #     user_form = UserEditForm(instance=user)
    # return render(request,'user_edit.html',{'user_form':user_form})
    if request.method == 'POST':
        user_form = UserEditForm(request.POST,instance=request.user.lab)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('user_view',args=(request.user.lab.id,)))
    else:
        user_form = UserEditForm(instance=request.user.lab)
    return render(request,'user_edit.html',{'user_form':user_form})

# @login_required
def user_add(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            school_num = form.cleaned_data['school_num']
            # name = form.cleaned_data['name']
            role = form.cleaned_data['role']
            user = User.objects.create_user(std_id=school_num, password=school_num)
            teacher = Group.objects.get(name='teacher')
            student = Group.objects.get(name='student')
            # lab = Profile(user=user, name=name, role=role)
            # lab.save()
            if role==1:
                user.groups.add(teacher)
            if role==2:
                user.groups.add(student)
            user.save()

            return HttpResponseRedirect(reverse('user-list'))
    else:
        form = UserAddForm()
    return render(request,'user_add.html',{'form':form})

@login_required
@permission_required('lab.delete_labmember',raise_exception=True)
def user_del(request,d):
    user_id = Profile.objects.get(id = d).user_id
    Profile.objects.get(id = d).delete()
    User.objects.get(id = user_id).delete()
    return HttpResponseRedirect(reverse('user-list'))

@login_required
def user_list(request):
    lab_list = Profile.objects.all()
    return render(request,'user-list.html',{'lab_list':lab_list})