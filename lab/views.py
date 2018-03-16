# encoding:  utf-8
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import GoodAddForm,GoodEditForm,ProjectPulishForm,LoginForm,GoodBorrowForm,MessageAddForm
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import Good,Project,User,ProApprove,GoodBorrow,Message
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import permission_required,login_required

@login_required
def home_page(request):
    return render(request, 'home.html')

def login_view(request):
    error_msg = ""
    if request.method=='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['std_id']
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
        login_form = LoginForm()
    return render(request,'registration/login.html',{'login_form':login_form,'error_msg':error_msg})


@login_required
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_detail.html', {'user':user})

@login_required
def user_list(request):
    user_list = User.objects.all()
    return render(request, 'user_list.html', {'user_list':user_list})


@login_required
@permission_required('lab.delete_user',raise_exception=True)
def user_del(request,d):
    user_id = User.objects.get(id = d).user_id
    User.objects.get(id = d).delete()
    User.objects.get(id = user_id).delete()
    return HttpResponseRedirect(reverse('user-list'))


@login_required
def project_pulish(request):
    if request.method == 'POST':
        form = ProjectPulishForm(request.POST)
        if form.is_valid():
            form.save_it(request.user)#讲当前用户传进去作为leader，并且自动加入项目团队
            return HttpResponseRedirect(reverse('project-list'))
    else:
        form =ProjectPulishForm()
    return render(request, 'project_pulish.html', {'form':form})

@login_required
@permission_required('lab.delete_project',raise_exception=True)
def project_delete(request,id):
    Project.objects.get(id = id).delete()
    return HttpResponseRedirect(reverse('project-list'))

@login_required
@permission_required('lab.apply_project',raise_exception=True)
def project_apply(request, id):
    p = Project.objects.get(id = id)
    ProApprove.objects.create(project=p,user=request.user)
    return HttpResponseRedirect(reverse('project-list'))

@login_required
def project_message(request):
    p = ProApprove.objects.filter(project__leader=request.user).filter(status=2)
    return render(request, 'project_msg.html', {'pro_approves':p})

@login_required
@csrf_exempt
def project_approve(request):
    id = request.POST.get('id')
    status = request.POST.get('status')
    if int(status)==0:
        ProApprove.objects.filter(id = id).update(status=0)
    else:
        ProApprove.objects.filter(id = id).update(status=1)
    return HttpResponse('ok')

@login_required
def project_mine(request):
    p = Project.objects.filter(users__id=request.user.id)
    return render(request, 'project_mine.html', {'projects':p})

@login_required
def project_list(request):
    plist = Project.objects.all()
    per_page = 20
    paginator = Paginator(plist,per_page)
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return render(request, 'project_list.html', {'projects':projects})

def project_detail(request, id):
    project = Project.objects.get(id = id)
    return render(request, 'project_detail.html', {'project':project})

@login_required
def good_list(request):
    good_list = Good.objects.all()
    per_page = 15
    paginator = Paginator(good_list,per_page)
    page = request.GET.get('page')
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        goods = paginator.page(1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)
    return render(request, 'good-list.html', {'goods':goods})

def good_detail(request,id):
    good = Good.objects.filter(id = id).first()
    return render(request,'good_detail.html',{'good':good})

def good_search(request):
    return


def good_apply(request,id):
    error = ''
    good  = Good.objects.filter(id = id).first()
    if request.method=='POST':
        f  =GoodBorrowForm(request.POST)
        if f.is_valid():
            num = f.cleaned_data['num']
            st = f.cleaned_data['start_t']
            et = f.cleaned_data['end_t']
            if num>good.active_num:
                error = u'数量不够了'
            else:
                GoodBorrow.objects.create(user=request.user,good=good,num=num,start_t=st,end_t=et)
                return HttpResponseRedirect(reverse('good-list'))
    else:
        f = GoodBorrowForm()
    return render(request,'good_apply.html',{'form':f,'error_msg':error,'good':good})

def good_message(request):
    g = GoodBorrow.objects.filter(status=2)
    return render(request,'good_msg.html',{'g':g})

@login_required
@csrf_exempt
@permission_required('lab.delete_good',raise_exception=True)
def good_del(request):
    id = request.POST.get('id')
    Good.objects.get(id = id).delete()
    return HttpResponse("delete success!")

@login_required
@permission_required('lab.change_good',raise_exception=True)
def good_edit(request, id):
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


def message_list(request):
    messages_l = Message.objects.all()
    per_page = 5
    paginator = Paginator(messages_l,per_page)
    page = request.GET.get('page')
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)
    return render(request, 'message-list.html',{'msgs':messages})

def message_push(request):
    if request.method == 'POST':
        form = MessageAddForm(request.POST)
        msg = form.save()
        msg.user = request.user
        msg.save()
        return HttpResponseRedirect(reverse('message-list'))
    else:
        form = MessageAddForm()
    return render(request, 'message-push.html', {'form':form})

def message_detail(request,id):
    msg = Message.objects.filter(id = id).first()
    return render(request,'message-detail.html',{'msg':msg})

