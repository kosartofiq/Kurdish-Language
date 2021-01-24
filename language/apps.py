from django.apps import AppConfig


class LanguageConfig(AppConfig):
    name = 'language'

    # for work of signal save
    def ready(self):
        import language.signals
