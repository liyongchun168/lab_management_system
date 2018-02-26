# encoding:  utf-8
from django.shortcuts import render
from .forms import GoodAddForm,GoodEditForm,ProjectPulishForm
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import Good,ProjectTeam
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import permission_required,login_required

@login_required
def home_page(request):
    return render(request, 'home_page.html')



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
    Good.objects.get(id = id).delete()
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


