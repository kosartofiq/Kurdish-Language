from django.contrib import admin
from .models import Language, LanguageHistory, Dialect, DialectHistory

# Register your models here.
admin.site.register(Language)
admin.site.register(LanguageHistory)
admin.site.register(Dialect)
admin.site.register(DialectHistory)
