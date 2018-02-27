
from django.apps import AppConfig


class LabCongig(AppConfig):
    name = 'lab'
    def ready(self):
        import lab.signals