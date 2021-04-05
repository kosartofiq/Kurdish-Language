from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from global_functions import is_same
from .models import Book, BookHistory, BookWriter, BookWriterHistory, Page, PageHistory, Paragraph, ParagraphHistory, \
    Genre, GenreHistory, Job, JobHistory, Location, \
    LocationHistory, Publisher, PublisherHistory, Writer, WriterHistory


# #########################
# Book
# #########################
# @receiver(post_save, sender=Book)
def create_book_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        BookHistory.objects.create(
            editor=instance.creator,

            book=instance,
            location=instance.location,
            publisher=instance.publisher,
            genres=instance.genres.all,
            languages=instance.languages.set,
            writers=instance.writers.set,
            name=instance.name,
            description=instance.description,
            year=instance.year,
            edition_number=instance.edition_number,
            volume=instance.volume,
            part=instance.part,
            page_quantity=instance.page_quantity,
            is_copyright=instance.is_copyright,
            image=instance.image,
        )
        # Dialect.objects.create(language=instance,


# @receiver(pre_save, sender=Book)
def update_book_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not
    # make history
    # get object if is not first time creation
    old_record = Book.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if old_record.is_same(instance):
            # it means just clicked save without modification, so pass signal
            # and do nothing
            pass
        else:
            # create history
            BookHistory.objects.create(editor=instance.creator,
                                       book=instance,
                                       location=instance.location,
                                       publisher=instance.publisher,
                                       genres=instance.genres.set,
                                       languages=instance.language.set,
                                       writers=instance.writers.set,
                                       name=instance.name,
                                       description=instance.description,
                                       year=instance.year,
                                       edition_number=instance.edition_number,
                                       volume=instance.volume,
                                       part=instance.part,
                                       page_quantity=instance.page_quantity,
                                       is_copyright=instance.is_copyright,
                                       image=instance.image, )


# #########################
# Page
# #########################
@receiver(post_save, sender=Page)
def create_page_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        PageHistory.objects.create(
            page=instance,
            editor=instance.creator,
            number=instance.number,
            page_type=instance.page_type,
            preview_page=instance.preview_page,
            is_blank=instance.is_blank,
            is_finished=instance.is_finished,
            image=instance.image,
        )


@receiver(pre_save, sender=Page)
def update_page_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not
    # make history
    # get object if is not first time creation
    old_record = Page.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal
            # and do nothing
            pass
        else:
            # create history
            PageHistory.objects.create(
                page=instance,
                editor=instance.creator,
                number=instance.number,
                page_type=instance.page_type,
                preview_page=instance.preview_page,
                is_blank=instance.is_blank,
                is_finished=instance.is_finished,
                image=instance.image,
            )


# #########################
# Paragraph
# #########################
@receiver(post_save, sender=Paragraph)
def create_paragraph_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        ParagraphHistory.objects.create(
            paragraph=instance,
            editor=instance.creator,
            text=instance.text,
            preview_paragraph=instance.preview_paragraph,
            tail_paragraph=instance.tail_paragraph,
        )


@receiver(pre_save, sender=Paragraph)
def update_paragraph_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not
    # make history
    # get object if is not first time creation
    old_record = Paragraph.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal
            # and do nothing
            pass
        else:
            # create history
            ParagraphHistory.objects.create(
                paragraph=instance,
                editor=instance.creator,
                text=instance.text,
                preview_paragraph=instance.preview_paragraph,
                tail_paragraph=instance.tail_paragraph,
            )


# #########################
# Genre
# #########################
@receiver(post_save, sender=Genre)
def create_genre_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        GenreHistory.objects.create(genre=instance,
                                    editor=instance.creator,
                                    name=instance.name,
                                    description=instance.description)


@receiver(pre_save, sender=Genre)
def update_genre_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not
    # make history
    # get object if is not first time creation
    old_record = Genre.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal
            # and do nothing
            pass
        else:
            # create history
            GenreHistory.objects.create(genre=instance,
                                        editor=instance.creator,
                                        name=instance.name,
                                        description=instance.description)


# #########################
# Job
# #########################
@receiver(post_save, sender=Job)
def create_job_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        JobHistory.objects.create(job=instance,
                                  editor=instance.creator,
                                  name=instance.name,
                                  description=instance.description)


@receiver(pre_save, sender=Job)
def update_job_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not
    # make history
    # get object if is not first time creation
    old_record = Job.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal
            # and do nothing
            pass
        else:
            # create history
            JobHistory.objects.create(job=instance,
                                      editor=instance.creator,
                                      name=instance.name,
                                      description=instance.description)


# #########################
# Location
# #########################
@receiver(post_save, sender=Location)
def create_location_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        LocationHistory.objects.create(location=instance,
                                       editor=instance.creator,
                                       name=instance.name,
                                       description=instance.description)


@receiver(pre_save, sender=Location)
def update_location_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not
    # make history
    # get object if is not first time creation
    old_record = Location.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal
            # and do nothing
            pass
        else:
            # create history
            LocationHistory.objects.create(location=instance,
                                           editor=instance.creator,
                                           name=instance.name,
                                           description=instance.description)


# #########################
# Publisher
# #########################
@receiver(post_save, sender=Publisher)
def create_publisher_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        PublisherHistory.objects.create(publisher=instance,
                                        editor=instance.creator,
                                        name=instance.name,
                                        description=instance.description,
                                        logo=instance.logo)


@receiver(pre_save, sender=Publisher)
def update_publisher_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not
    # make history
    # get object if is not first time creation
    old_record = Publisher.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal
            # and do nothing
            pass
        else:
            # create history
            PublisherHistory.objects.create(publisher=instance,
                                            editor=instance.creator,
                                            name=instance.name,
                                            description=instance.description,
                                            logo=instance.logo)


# #########################
# Writer
# #########################
@receiver(post_save, sender=Writer)
def create_writer_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        WriterHistory.objects.create(writer=instance,
                                     editor=instance.creator,
                                     name=instance.name,
                                     born_date=instance.born_date,
                                     died_date=instance.died_date,
                                     profile=instance.profile,
                                     image=instance.image)


@receiver(pre_save, sender=Writer)
def update_writer_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not
    # make history
    # get object if is not first time creation
    old_record = Writer.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal
            # and do nothing
            pass
        else:
            # create history
            WriterHistory.objects.create(writer=instance,
                                         editor=instance.creator,
                                         name=instance.name,
                                         born_date=instance.born_date,
                                         died_date=instance.died_date,
                                         profile=instance.profile,
                                         image=instance.image)
