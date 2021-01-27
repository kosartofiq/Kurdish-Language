from django.contrib import admin

from .models import Book, BookWriter, BookHistory, BookWriterHistory, Genre, GenreHistory, Job, JobHistory, Location, \
    LocationHistory, Publisher, PublisherHistory, Writer, WriterHistory

admin.site.register(Book)
admin.site.register(BookWriter)
admin.site.register(BookHistory)
admin.site.register(BookWriterHistory)
admin.site.register(Genre)
admin.site.register(GenreHistory)
admin.site.register(Job)
admin.site.register(JobHistory)
admin.site.register(Location)
admin.site.register(LocationHistory)
admin.site.register(Publisher)
admin.site.register(PublisherHistory)
admin.site.register(Writer)
admin.site.register(WriterHistory)



