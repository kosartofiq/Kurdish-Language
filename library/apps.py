from django.apps import AppConfig


class LibraryConfig(AppConfig):
    name = 'library'

    # for work of signal save
    def ready(self):
        import library.signals
