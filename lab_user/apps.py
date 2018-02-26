from django.apps import AppConfig


class LabUserCongig(AppConfig):
    name = 'lab_user'
    def ready(self):
        import lab_user.signals