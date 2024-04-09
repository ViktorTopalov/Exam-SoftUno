from django.apps import AppConfig


class AccConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'final_exam_project.acc'


    def ready(self):
        import final_exam_project.acc.signals