from django.apps import AppConfig

class PlaygroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'

    def ready(self):
        # Move the import here to avoid circular logic
        import playground.signals
