"""lab_admin_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','lab.views.home_page', name='homepage'),
    url(r'^login/$','lab.views.login_view',name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/login/'},name='logout'),
    # url(r'^register/$','lab.views.register',name='register'),

    url(r'^good/list/$', 'lab.views.good_list', name='good-list'),
    url(r'^good/(\d+)','lab.views.good_detail',name='good_detail'),
    url(r'^good/del/$', 'lab.views.good_del', name='del_good'),
    url(r'^good/edit/(\d+)$', 'lab.views.good_edit', name='edit_good'),
    url(r'^good/reply/(\d+)$','lab.views.good_apply',name='good-reply'),
    url(r'^good/message$','lab.views.good_message',name='good-msg'),
    url(r'^money/$','lab.views.money',name='money'),
    url(r'^money/edit/(\d+)','lab.views.edit_money',name='edit_money'),
    url(r'^money/del/(\d+)','lab.views.del_money',name='del_money'),
    url(r'^project/list/$','lab.views.project_list',name='project-list'),
    url(r'^project/(\d+)$', 'lab.views.project_detail',name='project-detail'),
    url(r'^project/publish/$','lab.views.project_pulish',name='project-publish'),
    url(r'^project/del/(\d+)$','lab.views.project_delete',name='project-del'),
    url(r'^project/apply/(\d+)$','lab.views.project_apply',name='project-apply'),
    url(r'^project/message/$','lab.views.project_message',name='project-msg'),
    url(r'^project/approve/(\d+)/(\d)$','lab.views.project_approve',name='project-app'),
    url(r'^project/mine/$', 'lab.views.project_mine', name='project-mine'),

    url(r'^user/(\d+)', 'lab.views.user_detail', name='user-detail'),
    # url(r'^user/edit/$','lab.views.user_edit',name='user-edit'),
    # url(r'^user/add/$', 'lab.views.user_add', name='user-add'),
    # url(r'^user/del/(\d+)','lab.views.user_del',name='user-del'),
    url(r'^user/list/$', 'lab.views.user_list', name='user-list'),

    # url(r'^person/$','lab.views.person',name='person'),
    # url(r'^good/(\d*)/$','lab.views.good_detail',name='good_detail')

    # url(r'^student/$','lab.views.student',name='student'),
    # url(r'^test/$','lab.views.test',name='test')
    ]
