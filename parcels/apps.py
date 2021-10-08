from django.apps import AppConfig


class ParcelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parcels'

    def ready(self) -> None:
        import parcels.signals.handlers
