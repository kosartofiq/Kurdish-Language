from django.contrib import admin

from .models import Genre, GenreHistory, Job, JobHistory, Location, LocationHistory


admin.site.register(Genre)
admin.site.register(GenreHistory)
admin.site.register(Job)
admin.site.register(JobHistory)
admin.site.register(Location)
admin.site.register(LocationHistory)


