# encoding: utf-8
from django.apps import AppConfig


class LabCongig(AppConfig):
    name = 'lab'
    verbose_name = u'实验室管理系统'
    def ready(self):
        import lab.signals