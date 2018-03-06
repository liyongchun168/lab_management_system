# encoding:  utf-8
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import GoodAddForm,GoodEditForm,ProjectPulishForm,LoginForm,GoodBorrowForm
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import Good,Project,User,ProApprove,GoodBorrow
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
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_detail.html', {'user':user})

@login_required
def user_list(request):
    user_list = User.objects.all()
    return render(request, 'user_list.html', {'user_list':user_list})
# @login_required
# def user_edit(request):
#     #
#     # try:
#     #     user = LabMember.objects.get(id=user_id)
#     # except ObjectDoesNotExist:
#     #     return HttpResponseNotFound('404')
#     # if request.user.lab.id != user.id:#如果修改的用户不是当前用户就返回404
#     #     return HttpResponseNotFound('404没有找到')
#     # if request.method == 'POST':
#     #     user_form = UserEditForm(request.POST,instance=user)
#     #     if user_form.is_valid():
#     #         user_form.save()
#     #         return HttpResponseRedirect(reverse('user_view',args=(user_id,)))
#     # else:
#     #     user_form = UserEditForm(instance=user)
#     # return render(request,'user_edit.html',{'user_form':user_form})
#     if request.method == 'POST':
#         user_form = UserEditForm(request.POST,instance=request.user)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('user_view',args=(request.user.id,)))
#     else:
#         user_form = UserEditForm(instance=request.user)
#     return render(request,'user_edit.html',{'user_form':user_form})
#
# @login_required
# def user_add(request):
#     if request.method == 'POST':
#         form = UserAddForm(request.POST)
#         if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(reverse('user-list'))
#     else:
#         form = UserAddForm()
#     return render(request,'user_add.html',{'form':form})

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
def project_approve(request,p_id,status):
    if int(status)==1:
        ProApprove.objects.filter(id = p_id).update(status=1)
    if int(status)==0:
        ProApprove.objects.filter(id = p_id).update(status=0)
    return HttpResponseRedirect(reverse('project-msg'))

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
    # if request.method=='POST':
    #     form = GoodAddForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('good'))
    good_list = Good.objects.all()
    per_page = 20
    paginator = Paginator(good_list,per_page)
    page = request.GET.get('page')
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        goods = paginator.page(1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)
    return render(request, 'good-list.html', {'goods':goods})

def good_detail(request):
    return

def good_search(request):
    return

# def good_apply(request,id):
#     good = Good.objects.filter(id = id).first()
#     good_borrow = GoodBorrow.objects.create(good=good,user=request.user)
#     if request.method == 'POST':
#         f = GoodBorrowForm(request.POST)
#         if f.is_valid():
#             f.save()
#     else:
#         f = GoodBorrowForm(user_id=request.user.id,good_id=good.id)
#         return render(request,'good_apply.html',{'good':good,'goodf':f})
# def good_apply(request):
#     if request.method == 'POST':
#         f = GoodBorrowForm(request.POST)

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

@login_required
@permission_required('lab.delete_good',raise_exception=True)
def good_del(request, id):
    Good.objects.get(id = id).delete()
    return HttpResponseRedirect(reverse('good'))

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




