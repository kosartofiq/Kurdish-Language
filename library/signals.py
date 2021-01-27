from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from global_functions import is_same
from .models import (
    #Book,
    #BookHistory,
    #BookWriter,
    #BookWriterHistory,
    Genre,
    GenreHistory,
    Job,
    JobHistory,
    Location,
    LocationHistory,
    Publisher,
    PublisherHistory,
    Writer,
    WriterHistory
)

"""
@receiver(pre_save, sender=Book)
def update_book_history(sender, instance, **kwargs):
    # print('pre save called')
    # check if any change happen or only clicked save without change, to not make history
    # get object if is not first time creation
    old_record = Book.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if old_record.is_same(instance):
            # print('same')
            pass
        else:
            # print('different')
            BookHistory.objects.create(book=instance,
                                       editor=instance.creator,
                                       location=instance.location,
                                       publisher=instance.publisher,

                                       name=instance.name,
                                       description=instance.description,
                                       year=instance.year,
                                       publish_number=instance.publish_number,
                                       volume=instance.volume,
                                       part=instance.part,
                                       number_of_pages=instance.number_of_pages,
                                       is_copyright=instance.is_copyright
                                       )


@receiver(post_save, sender=Book)
def create_book_history(sender, instance, created, **kwargs):
    # print('post save called')
    # if new object created then make history
    if created:
        # create history
        BookHistory.objects.create(book=instance,
                                   editor=instance.creator,
                                   location=instance.location,
                                   publisher=instance.publisher,

                                   name=instance.name,
                                   description=instance.description,
                                   year=instance.year,
                                   publish_number=instance.publish_number,
                                   volume=instance.volume,
                                   part=instance.part,
                                   number_of_pages=instance.number_of_pages,
                                   is_copyright=instance.is_copyright
                                   )
        # Dialect.objects.create(language=instance,

"""


# #########################
# Genre
# #########################
@receiver(post_save, sender=Genre)
def create_genre_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        GenreHistory.objects.create(
            genre=instance,
            editor=instance.creator,
            name=instance.name,
            description=instance.description
        )


@receiver(pre_save, sender=Genre)
def update_genre_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not make history
    # get object if is not first time creation
    old_record = Genre.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal and do nothing
            pass
        else:
            # print('different')
            GenreHistory.objects.create(
                genre=instance,
                editor=instance.creator,
                name=instance.name,
                description=instance.description
            )


# #########################
# Job
# #########################
@receiver(post_save, sender=Job)
def create_job_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        JobHistory.objects.create(
            job=instance,
            editor=instance.creator,
            name=instance.name,
            description=instance.description
        )


@receiver(pre_save, sender=Job)
def update_job_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not make history
    # get object if is not first time creation
    old_record = Job.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal and do nothing
            pass
        else:
            # print('different')
            JobHistory.objects.create(
                job=instance,
                editor=instance.creator,
                name=instance.name,
                description=instance.description
            )


# #########################
# Location
# #########################
@receiver(post_save, sender=Location)
def create_location_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        LocationHistory.objects.create(
            location=instance,
            editor=instance.creator,
            name=instance.name,
            description=instance.description
        )


@receiver(pre_save, sender=Location)
def update_location_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not make history
    # get object if is not first time creation
    old_record = Location.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal and do nothing
            pass
        else:
            # print('different')
            LocationHistory.objects.create(
                location=instance,
                editor=instance.creator,
                name=instance.name,
                description=instance.description
            )


# #########################
# Publisher
# #########################
@receiver(post_save, sender=Publisher)
def create_publisher_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        PublisherHistory.objects.create(
            publisher=instance,
            editor=instance.creator,
            name=instance.name,
            description=instance.description,
            logo=instance.logo
        )


@receiver(pre_save, sender=Publisher)
def update_publisher_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not make history
    # get object if is not first time creation
    old_record = Publisher.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal and do nothing
            pass
        else:
            # print('different')
            PublisherHistory.objects.create(
                publisher=instance,
                editor=instance.creator,
                name=instance.name,
                description=instance.description,
                logo=instance.logo
            )


# #########################
# Writer
# #########################
@receiver(post_save, sender=Writer)
def create_writer_history(sender, instance, created, **kwargs):
    # if new object created then make history
    if created:
        # create history
        WriterHistory.objects.create(
            writer=instance,
            editor=instance.creator,
            name=instance.name,
            born_date=instance.born_date,
            died_date=instance.died_date,
            profile=instance.profile,
            image=instance.image
        )


@receiver(pre_save, sender=Writer)
def update_writer_history(sender, instance, **kwargs):
    # check if any change happen or only clicked save without change, to not make history
    # get object if is not first time creation
    old_record = Writer.objects.filter(id=instance.id).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal and do nothing
            pass
        else:
            # print('different')
            WriterHistory.objects.create(
                writer=instance,
                editor=instance.creator,
                name=instance.name,
                born_date=instance.born_date,
                died_date=instance.died_date,
                profile=instance.profile,
                image=instance.image)


