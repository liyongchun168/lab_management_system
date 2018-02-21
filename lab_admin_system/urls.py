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
    url(r'^register/$','lab.views.register',name='register'),
    url(r'^good/$','lab.views.good_view',name='good'),
    url(r'^good/del/(\d*)$','lab.views.del_good',name='del_good'),
    url(r'^good/edit/(\d*)$','lab.views.edit_good',name='edit_good'),
    url(r'money/$','lab.views.money',name='money'),
    url(r'money/edit/(\d+)','lab.views.edit_money',name='edit_money'),
    url(r'money/del/(\d+)','lab.views.del_money',name='del_money'),
    # url(r'^person/$','lab.views.person',name='person'),
    # url(r'^good/(\d*)/$','lab.views.good_detail',name='good_detail')

    # url(r'^student/$','lab.views.student',name='student'),
    url(r'^test/$','lab.views.test',name='test')
    ]
