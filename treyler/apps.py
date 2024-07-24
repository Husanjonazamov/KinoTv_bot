from django.apps import AppConfig



class TreylerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'treyler'

    def ready(self):
        import treyler.signals


