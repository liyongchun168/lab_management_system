# encoding:  utf-8
from django.shortcuts import render
from .forms import Login_form,Register_form,GoodAddForm,GoodEditForm,ProjectPulishForm
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError,models
from .models import LabMember,Good,ProjectTeam
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import permission_required,login_required

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

def register(request):
    error_msg = ''
    if request.method=='POST':
        try:
            LabMember.creat_group()
        except IntegrityError:
            pass
        register_form = Register_form(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['name']
            password = register_form.cleaned_data['password']
            user_group = register_form.cleaned_data['user_group']
            try:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                try:
                    group = Group.objects.get(name=user_group)
                    user.groups.add(group)
                    user.save()
                    return HttpResponseRedirect(reverse('login'))
                except Exception:
                    error_msg = u'用户角色设置错误'
            except IntegrityError:
                error_msg = u'该账号已被注册'
            except Exception:
                error_msg = u'出现内部错误,请稍后再试'
    else:
        register_form = Register_form()
    return render(request,'registration/register.html',{'register_form':register_form,'error_msg':error_msg})

def home_page(request):
    return render(request, 'home_page.html')

@login_required
def good_view(request):
    if request.method=='POST':
        form = GoodAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('good'))
    good_list = Good.objects.all()
    per_page = 5
    paginator = Paginator(good_list,per_page)
    page = request.GET.get('page')
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        goods = paginator.page(1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)
    return render(request,'good.html',{'goods':goods})

@login_required
@permission_required('lab.delete_good',raise_exception=True)
def del_good(request,id):
    Good.objects.get(id = int(id)).delete()
    return HttpResponseRedirect(reverse('good'))

@login_required
@permission_required('lab.change_good',raise_exception=True)
def edit_good(request,id):
    if request.method == 'POST':
        try:
            good = Good.objects.get(id = id)
        except ObjectDoesNotExist:
            return HttpResponseForbidden('禁止')
        form = GoodEditForm(request.POST,instance=good)
        form.save()
        return HttpResponseRedirect(reverse('good'))
    else:

        good = Good.objects.get(id = id)
        form = GoodEditForm(instance=good)
        return render(request,'good_edit.html',{'form':form})

def money(request):
    pass
def edit_money(request):
    pass
def del_money(request):
    pass

def project_pulish(request):
    if request.method == 'POST':
        form = ProjectPulishForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project-list'))
    else:
        form =ProjectPulishForm()
    return render(request,'project_pulish.html',{'form':form})

def project_list(request):
    plist = ProjectTeam.objects.all()
    per_page = 5
    paginator = Paginator(plist,per_page)
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return render(request,'project-list.html',{'projects':projects})

def test(request):
    return HttpResponseForbidden('403禁止')